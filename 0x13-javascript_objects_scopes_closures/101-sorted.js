#!/usr/bin/node
const dict = require('./101-data').dict;

const totalist = Object.entries(dict);
const vals = Objects.values(dict);
const valsUniq = [...new Set(vals)];
const newDict = {};
for (const j in valsUniq) {
	const list = [];
	for (const k in totalist) {
		if (totallist[k][1] === valsUniq[j]) {
			list.unshift(totalist[k][0]);
		}
	}
	newDict[valsUniq[j]] = list;
}
console.log(newDict);
