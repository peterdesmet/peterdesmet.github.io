Title: Analyzing the licenses of all 11.000+ GBIF datasets
Slug: analyzing-gbif-data-licenses
Date: 2013-11-20 11:00
Author: Peter Desmet
Tags: Open data, GBIF
Summary: ...
Status: draft

<script src="http://d3js.org/d3.v3.min.js"></script>
<script src="http://datafable.github.io/gbif-data-licenses/charts/js/nv.d3.min.js"></script>
<script src="http://datafable.github.io/gbif-data-licenses/charts/js/charts.js"></script>
<link href="http://datafable.github.io/gbif-data-licenses/charts/css/nv.d3.min.css" rel="stylesheet" type="text/css">

In my [previous post](|filename|illegal-bullfrogs.md), I highlighted the legal issues showing 13,297 American bullfrog records downloaded from [GBIF](http://www.gbif.org) on a map. 96% of those records had no or a non-standard data license, making even basic data use legally unnecessarily difficult. But how much of this applies to all [417+ million occurrence records](http://www.gbif.org/occurrence) in GBIF? How much of it is open data?  Fellow Datafable[^1] member Bart Aelterman and I tried to figure out.

[^1]: Datafable ...

All code and data ...

* GitHub
* Guidelines

## Standard licenses

<div class="clearfix">
    <svg id="chart1" class="chart" style="float:left; width: 50%;"></svg>
    <svg id="chart2" class="chart" style="float:left; width: 50%;"></svg>
</div>

* % licenses, datasets, occurrences with standard license
* Breakdown of licenses (table)
* Breakdown public domain (recommended), open data, GBIF practice

## Use within GBIF network

* Legal? Somewhere between licenses and norms
* Interpretation of `not supplied`
* Bar chart of parameters for datasets, occurrences
* Breakdown public domain, open data, GBIF practice

## Universal use

<div><svg id="chart3" class="chart"></svg></div>

<div><svg id="chart4" class="chart"></svg></div>

* Other interpretation of `not supplied`
* Bar chart of parameters for datasets, occurrences
* Breakdown public domain, open data, GBIF practice

## Next steps

* GBIF 2014 work program
* Easy translation
* Hard translation
* Machine tags
* Contribute and pick apart GitHub
