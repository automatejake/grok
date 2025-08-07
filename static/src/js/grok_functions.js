/** @odoo-module **/

import * as spreadsheet from "@odoo/o-spreadsheet";
import { addFunction} from "@odoo/o-spreadsheet";
import { _t } from "@web/core/l10n/translation";
import { OdooUIPlugin } from "@spreadsheet/plugins";

const { arg, toString } = spreadsheet.helpers;
const { featurePluginRegistry } = spreadsheet.registries;

export class GrokPlugin extends OdooUIPlugin {
    static getters = ["grokRequest"];

    constructor(config) {
        super(config);
        this.cache = {};
    }

    getFromCache(query) {
        if (query in this.cache) {
            return this.cache[query];
        }
        return { status: "missing" };
    }

    fetchGrokRequest(query){
        const url = "/spreadsheet/grok";
        this.cache[query] = { status: "pending" };
        fetch(url, {
            method: "POST",
            body: JSON.stringify(
                {'prompt': query}
            )
            ,
            headers: {
                "Content-Type": "application/json",
            }
        }).then((response) => response.json()
            .then((data) => {
                if(data.result.error)
                    this.cache[query] = {
                        "status":"error",
                        "error":data.result.error,
                    }
                else 
                    this.cache[query] = {
                        "status":"success",
                        "value": data.result
                    }}))
            .catch((error) => {
                this.cache[query] = {
                    "status":"error",
                    error
                }})
            .finally(() => {
                this.dispatch("EVALUATE_CELLS");
            });

    }

    grokRequest(query) {
        const rate = this.getFromCache(query);
        switch (rate.status) {
            case "missing":
              this.fetchGrokRequest(query);
            case "pending":
            case "success":
                return rate.value;
            case "error":
                return rate.error;
            default:
              throw new Error("An unexpected error occurred");
          }
    }
}

featurePluginRegistry.add("odooGrok", GrokPlugin);

const grokai = {
    description: _t("Groom Excel data with Grok AI"),
    args: [
        arg("string1 (string, range<string>)", _t("The initial string.")),
        arg("string2 (string, range<string>, repeating)", _t("More strings to append in sequence.")),
    ],
    returns: ["STRING"],
    compute: function (...datas) {
        const query = datas
            .flat(Infinity)
            .map(a => toString(a))
            .filter((s) => s)
            .join(" ")

        return this.getters.grokRequest(query)
    },
    isExported: false
};

addFunction("GROKAI", grokai);