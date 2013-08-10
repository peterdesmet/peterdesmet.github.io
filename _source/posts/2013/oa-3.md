Title: Finding open access research articles
Slug: oa-3
Date: 2013-08-10 22:00
Author: Peter Desmet
Tags: Open science course, Open access
Summary: Not all search tools are equal. Also, the advantage of standard licenses.

*Note: This post is a response to [this task](https://p2pu.org/en/courses/5/content/367/) of an [online course on open science](https://p2pu.org/en/courses/5/open-science-an-introduction/) I am following.*

As an exercise, I searched for open access (OA) research articles published after `2008` and related to `"GBIF" AND "data quality"`.

## Search tools

I tried four search tools:

Search tool | Results | OA filter
--- | --- | ---
[Google Scholar](http://scholar.google.com/scholar?as_q=gbif+%22data+quality%22&as_occt=any&as_ylo=2009&as_yhi=2013) | 332 | no[^1]
[ScienceDirect](http://www.sciencedirect.com/science?_ob=ArticleListURL&_method=list&_ArticleListID=-329228712&_sort=r&_st=4&_acct=C000059224&_version=1&_urlVersion=0&_userid=2932513&md5=1ef663bb9bac18a3eb8260442c743c30&searchtype=a) | 100 | no[^2]
[PubMed Central](http://www.ncbi.nlm.nih.gov/pmc/?term=GBIF+AND+data+quality+AND+%222009%22%5BPublication+Date%5D+%3A+%223000%22%5BPublication+Date%5D+AND+%22open+access%22%5BFilter%5D) | 148 | [yes](http://www.ncbi.nlm.nih.gov/pmc/tools/openftlist/)
[DOAJ](http://www.doaj.org/doaj?func=advancedSearch&uiLanguage=en&fromWeb=1&first=1&query1=GBIF&field1=all&bool1=AND&query2=data+quality&field2=all&pubYear=rangeYears&fromYear=2009&toYear=2013) | 5 | OA only

I found it surprising that not all of these offer the option to filter on `open access only`. I am curious to know if this is mostly because of technical or social limitations.

[^1]: Although [Google Scholar](http://scholar.google.com/) does not provide an OA filter, it clearly indicates which search results can be accessed for free, by providing a link on the right hand side (which includes the provider and format).
[^2]: [ScienceDirect](http://www.sciencedirect.com/) does indicate which search results have `Full-text available`.

## Finding the license

For three articles, I dug a little deeper to find the license. Two of these use and clearly indicate [Creative Commons Attribution](http://creativecommons.org/licenses/by/3.0/) (coincidentally these two were not find by ScienceDirect):

> Hill A.W., Guralnick R., Flemons P., Beaman R., Wieczorek J., Ranipeta A., Chavan V., & Remsen D. (2009). Location, location, location: utilizing pipelines and services to more effectively georeference the world's biodiversity data. BMC Bioinformatics, 10(Suppl 14), S3. doi: [10.1186/1471-2105-10-S14-S3](http://dx.doi.org/10.1186/1471-2105-10-S14-S3)

> Belbin L., Daly J., Hirsch T., Hobern D., & La Salle J. (2013). A specialist’s audit of aggregated occurrence records: An ‘aggregator’s’ perspective. Zookeys (305), 67-76. doi: [10.3897/zookeys.305.5438](http://dx.doi.org/10.3897/zookeys.305.5438)

The other one:

> Costello M.J., Michener W.K., Gahegan M., Zhang Z., & Bourne P.E. (2013). Biodiversity data should be published, cited, and peer reviewed. Trends in Ecology & Evolution, 28(8), 454-461. doi: [10.1016/j.tree.2013.05.002](http://dx.doi.org/10.1016/j.tree.2013.05.002)

... (which was not found via PubMed Central and DOAJ) can be downloaded as pdf (= OA), but if you actually want to do something with the content, you have to [indicate in a very detailed manner](https://s100.copyright.com/AppDispatchServlet?publisherName=ELS&contentID=S0169534713001092&orderBeanReset=true) what you want to (re)use the article for. Very few use cases seem to be free. In other words: yuck!

I am quite familiar with the [Creative Commons licenses](creativecommons.org/licenses/), but now I realize what a mess you get if those aren't applied. This OA article also demonstrates that the term "open access" doesn't tell you that much: there's still a whole range of [how open something really is](|filename|oa-2.md).
