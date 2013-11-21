Title: Analyzing the licenses of all 11,000+ GBIF registered datasets
Slug: analyzing-gbif-data-licenses
Date: 2013-11-22 11:00
Author: Peter Desmet
Tags: Open data, Open research, GBIF, Datafable
Summary: How much GBIF mediated data can be legally used easily? A collaborative analysis.

<script src="http://d3js.org/d3.v3.min.js"></script>
<script src="http://datafable.com/gbif-data-licenses/charts/js/nv.d3.min.js"></script>
<script src="http://datafable.com/gbif-data-licenses/charts/js/data.js"></script>
<script src="http://datafable.com/gbif-data-licenses/charts/js/charts.js"></script>
<link href="http://datafable.com/gbif-data-licenses/charts/css/nv.d3.min.css" rel="stylesheet" type="text/css">

In my [previous post](|filename|illegal-bullfrogs.md), I highlighted the legal issues showing 13,297 American bullfrog records downloaded from [GBIF](http://www.gbif.org) on a map. 96% of those records had no or a non-standard data license, making data use legally cumbersome.

But how much of this applies to all [417+ million occurrence records](http://www.gbif.org/occurrence) in GBIF? How challenging is GBIF's [2014 mission to provide a machine readable, standard license](|filename|gbif-data-license.md) for all datasets? Fellow Datafable[^1] member [Bart Aelterman](https://twitter.com/bartaelterman) and I tried to figure out.

[^1]: To combine our skills and organize some of our extracurricular activities, we started a team of open data enthusiasts called [Datafable](https://twitter.com/datafable). The results of our first project was [published by GBIF](http://www.gbif.org/page/2991) last week.

## Methodology

We used the [GBIF registry API](http://www.gbif.org/developer/registry) to obtain the metadata for all [11,000+ GBIF registered datasets](http://www.gbif.org/dataset/) and in particular the `rights` field, which is where data publishers can provide the license under which the dataset is published. We then created a [unique list of all licenses](https://github.com/Datafable/gbif-data-licenses/blob/master/data/licenses.csv) used, which we annotated with parameters such as `use allowed`and `attribution required`. This information was joined back with the dataset information to get an idea of the distribution of certain types of licenses over all datasets and occurrence records. We also documented the [guidelines](https://github.com/Datafable/gbif-data-licenses/blob/master/guidelines.md) we used for annotating these licenses.

In total we analyzed **11,974 datasets**[^2], representing **415,927,654 occurrences**. The first thing we noticed is that only 10% of those datasets (26% of the occurrences) have a license. This is problematic (see further), but it had the welcome side effect that we "only" had to [annotate 432 different licenses](https://github.com/Datafable/gbif-data-licenses/blob/master/data/licenses.csv).

[^2]: These include [checklist](http://www.gbif.org/dataset/search?type=CHECKLIST) and [occurrence datasets](http://www.gbif.org/dataset/search?type=OCCURRENCE). Obviously, only occurrence datasets are represented in the results for occurrences.

All code and data[^3] for this project are available on [GitHub](https://github.com/Datafable/gbif-data-licenses). #openresearch #ftw

[^3]: Additional legal issue: what license applies to the **metadata** of GBIF registered datasets? Can we publish even part of it on a GitHub repository? Note that metadata *does* include creative content, and some of it is even published as data papers.

## Results

### Overview of the licenses used

License | # of datasets | # of records | % of records | [GBIF practice?](https://dl.dropboxusercontent.com/u/639486/GBIF_Consultation_Standard_Data_Licences.pdf) | [Open data?](http://opendefinition.org/okd/)
--- | ---: | ---: | ---: | --- | ---
[CC0](http://creativecommons.org/publicdomain/zero/1.0/) | 105 | 2,155,108 | 0.5% | yes | yes
[CC BY](http://creativecommons.org/licenses/by/3.0/) | 8 | 2,240,674 | 0.5% | yes | yes
[ODC-By](http://opendatacommons.org/licenses/by/1.0/) | 11 | 567,675 | 0.1% | yes | yes
[CC BY-SA](http://creativecommons.org/licenses/by-sa/3.0/) | 16 | 450,421 | 0.1 | no | yes
[ODbL](http://opendatacommons.org/licenses/odbl/1.0/) & [DbCL](http://opendatacommons.org/licenses/dbcl/1.0/) | 3 | 864 | 0.0% | no | yes
[CC BY-NC](http://creativecommons.org/licenses/by-nc/3.0/) | 10 | 4,308,627 | 1.0% | expected by some | no
[CC BY-NC-SA](http://creativecommons.org/licenses/by-nc-sa/3.0/) | 17 | 569,040 | 0.1% | no | no
[CC BY-NC-ND](http://creativecommons.org/licenses/by-nc-nd/3.0/) | 1 | 26,132 | 0.0% | no | no
Non-standard license | 1,069 | 100,062,731 | 24.1% | ? | ?
No license | 10,734 | 305,546,382 | 73.5% | ? | ?

### Standard licenses

Ignoring for a moment that [CC0 is](http://www.canadensys.net/2012/why-we-should-publish-our-data-under-cc0) [the only](http://blog.datadryad.org/2011/10/05/why-does-dryad-use-cc0/) [sensible license](http://doi.org/10.6084/m9.figshare.799766) [for data](|filename|gbif-data-license.md), a standard license ([Creative Commons](http://creativecommons.org/licenses/) or [Open Data Commons](http://opendatacommons.org/licenses/)) is at least standardized and easy to understand. Only 1.4% of all datasets however (2% of all occurrences) are published with a standard license.

<div class="clearfix">
    <svg id="chart1" class="chart" style="float:left; width: 50%;"></svg>
    <svg id="chart2" class="chart" style="float:left; width: 50%;"></svg>
</div>

Data dedicated to the public domain under [CC0](http://creativecommons.org/publicdomain/zero/1.0/) represents an even smaller percentage: 0.9% of all datasets (0.5% of all occurrences). The silver lining is that most data publishers who choose a standard license, choose CC0 (105 datasets).

### Interpreting the other licenses

All other data are provided with no or a non-standard license, with a percentage similar to the [bullfrog sample](|filename|illegal-bullfrogs.md) (98% vs 96% of the occurrences). These data are in a legal gray zone: it's a mixture of legalese, norms, restrictions, agreements, or in most cases no information at all. It is up to every data user to figure out the details.

We tried to lift some of that burden by [interpreting all these licenses](https://github.com/Datafable/gbif-data-licenses/blob/master/data/licenses.csv), extracting some characteristics, but it should be clear that this is an attempt[^4] that should only be used with caution. The results are presented in the charts below. You can click the legends to toggle parts of the chart.

[^4]: We considered an alternative interpretation, taking into account the [GBIF use agreement](http://www.gbif.org/disclaimer/datause) (DUA). [Jonathan A. Rees](https://twitter.com/jar346) pointed out however that a DUA can only add restrictions or conditions, but never grant permissions (only copyright holders have the legal standing to do so). In other words, the GBIF DUA does not solve the situation of having no license: users still have the figure out the legal implications. See [this issue](https://github.com/Datafable/gbif-data-licenses/issues/12) for the whole discussion.

#### Datasets

<div><svg id="chart3" class="chart"></svg></div>

#### Occurrences

<div><svg id="chart4" class="chart"></svg></div>

## Conclusion

Our analysis of the licenses of all 11.000+ GBIF registered datasets shows a bleak picture. Very few GBIF registered datasets can be easily and legally used, let alone without restrictions. This is mainly due to data being published with no or a non-standard license.

Fixing this is crucial, and GBIF's 2014 mission to provide a machine readable, standard license to all datasets is a step in the good direction. We hope our [analysis](https://github.com/Datafable/gbif-data-licenses) (which can be run again) and [guidelines](https://github.com/Datafable/gbif-data-licenses/blob/master/guidelines.md) already help with:

> The Secretariat would review existing metadata provisionally to assign[^5] each current data set to one of these categories and would then communicate with data publishers to confirm the assignment. [[source](https://dl.dropboxusercontent.com/u/639486/GBIF_Consultation_Standard_Data_Licences.pdf)]

[^5]: The characteristics we assigned to the licenses (`commercial use allowed`, `notification required`, etc.) could even be provided as machine tags on the GBIF portal, allowing users to already get some indication of what is allowed/required.

More importantly, this mission should be used as [an opportunity](|filename|gbif-data-license.md) to make the `rights` field mandatory, require CC0, and shift the discussion about ethical data use (including attribution) to norms rather than ill-suited legal tools.
