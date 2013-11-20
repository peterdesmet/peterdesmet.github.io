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

In my [previous post](|filename|illegal-bullfrogs.md), I highlighted the legal issues showing 13,297 American bullfrog records downloaded from [GBIF](http://www.gbif.org) on a map. 96% of those records had no or a non-standard data license, making data use legally cumbersome. But how much of this applies to all [417+ million occurrence records](http://www.gbif.org/occurrence) in GBIF? How challenging is GBIF's [2014 mission to provide a machine readable license](|filename|gbif-data-license.md) for all datasets? Fellow Datafable[^1] member Bart Aelterman and I tried to figure out.

[^1]: To combine our skills and organize some of our extracurricular activities, we started a team of open data enthusiasts called [Datafable](https://twitter.com/datafable). The results of our first project was [published by GBIF](http://www.gbif.org/page/2991) last week.

## Methodology

All code and data[^2] for this project are available on [GitHub](https://github.com/Datafable/gbif-data-licenses). #openresearch #ftw

[^2]: Additional legal issue: what license applies to the **metadata** of GBIF registered datasets? Can we publish even part of it on a GitHub repository? Note that metadata *does* include creative content, and some of it is even published as data papers.

We used the [GBIF registry API](http://www.gbif.org/developer/registry) to obtain the metadata for all [11.000+ GBIF registered datasets](http://www.gbif.org/dataset/) and in particular the `rights` field, which is where data publishers can provide the license under which the dataset is published. We then created a [unique list of all licenses](https://github.com/Datafable/gbif-data-licenses/blob/master/data/licenses.csv) used, which we annotated with parameters such as `use allowed`and `attribution required`. This information was joined back with the dataset information to get an idea of the distribution of certain types of licenses over all datasets and occurrence records. We also documented the [guidelines](https://github.com/Datafable/gbif-data-licenses/blob/master/guidelines.md) we used for annotating these licenses.

In total we analyzed 11.972 datasets[^3] and 415.412.644 occurrences. The first thing we noticed is that only 10% of those datasets (26% of the occurrences) have a license. This is problematic (more on how to interpret this further in this post), but it had the welcome side effect that we "only" had to annotate 428 different licenses.

[^3]: These include [checklist](http://www.gbif.org/dataset/search?type=CHECKLIST) and [occurrence datasets](http://www.gbif.org/dataset/search?type=OCCURRENCE). Obviously, only occurrence datasets are represented in the results for occurrences.

## Standard licenses

Ignoring for a moment that [CC0 is](http://www.canadensys.net/2012/why-we-should-publish-our-data-under-cc0) [the only](http://blog.datadryad.org/2011/10/05/why-does-dryad-use-cc0/) [sensible license](http://doi.org/10.6084/m9.figshare.799766) [for data](|filename|gbif-data-license.md), a [Creative Commons](http://creativecommons.org/licenses/) or [Open Data Commons](http://opendatacommons.org/licenses/) license is at least standardized, legally valid, and easy to understand. Only 1% of the datasets (2% of the occurrences) however are published with a standard license.

<div class="clearfix">
    <svg id="chart1" class="chart" style="float:left; width: 50%;"></svg>
    <svg id="chart2" class="chart" style="float:left; width: 50%;"></svg>
</div>

This is an overview of the standard licenses used:

License | # of datasets | # of records | % of records | [GBIF practice?](https://dl.dropboxusercontent.com/u/639486/GBIF_Consultation_Standard_Data_Licences.pdf) | [Open data?](http://opendefinition.org/okd/)
--- | --- | --- | --- | --- | ---
[CC0](http://creativecommons.org/publicdomain/zero/1.0/) |||| yes | yes
[CC BY](http://creativecommons.org/licenses/by/3.0/) |||| yes | yes
[ODC-By](http://opendatacommons.org/licenses/by/1.0/) |||| yes | yes
[CC BY-SA](http://creativecommons.org/licenses/by-sa/3.0/) |||| no | yes
[ODbL](http://opendatacommons.org/licenses/odbl/1.0/) & [DbCL](http://opendatacommons.org/licenses/dbcl/1.0/) |||| no | yes
[CC BY-NC](http://creativecommons.org/licenses/by-nc/3.0/) |||| expected by some | no
[CC BY-NC-SA](http://creativecommons.org/licenses/by-nc-sa/3.0/) |||| no | no
[CC BY-NC-ND](http://creativecommons.org/licenses/by-nc-nd/3.0/) |||| no | no

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
