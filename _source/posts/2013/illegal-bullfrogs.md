Title: I cannot show you this bullfrog occurrence map for legal reasons
Slug: illegal-bullfrogs
Date: 2013-10-15 10:00
Author: Peter Desmet
Tags: Open data, GBIF
Summary: The problem with non-standard data licenses
Status: draft

Last week, the Global Biodiversity Information Facility (GBIF) launched their [new awesome data portal](http://www.gbif.org/). One of the things I like most is that the record limit on downloads has been lifted, so we now have free and open access to all 415+ occurrence records GBIF aggregates. GBIF also makes an effort to lower the barrier to correctly attribute the data publishers, by providing extensive metadata and a citation suggestion in each data download.

That doesn't mean however that it is actually easy to legally use the data, [something GBIF is well aware of](filename|gbif-data-license.md). As a test, I downloaded all [13,297 georeferenced American bullfrog records](http://www.gbif.org/occurrence/search?GEOREFERENCED=true&SPATIAL_ISSUES=false&TAXON_KEY=2427091) and would like to visualize and share these on a map using [CartoDB](http://cartodb.com). Technically, this would only take me a few minutes, but to make sure I'm not violating any restrictions, I need to take a closer look at the fine print.

## 65 data licenses

By downloading data from GBIF, I agree with the [data use agreement](http://www.gbif.org/disclaimer/datause), which states among other things: 

> * Users must comply with additional terms and conditions of use set by the Data Publisher. Where these exist they will be available through the metadata associated with the data.

Indeed, GBIF includes metadata for each dataset included in my download and a file with all the rights as supplied by the data publishers (`rights.txt`). Since my download aggregates records from 65 data publishers, I have to read and understand 65 rights statements before I can use the data[^1].

[^1]: Sadly, these rights are not attached to the data itself (maybe to prevent file size bloat), so I had to manually match (with some help of [Open Refine](http://openrefine.org/)) each `dataset_id` with the metadata in order to have the rights per record.
