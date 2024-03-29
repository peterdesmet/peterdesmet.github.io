---
title: Showing you this map of aggregated bullfrog occurrences would be illegal
description: Non-standard data licenses are a burden for users of aggregated GBIF data.
background:
  img: https://inaturalist-open-data.s3.amazonaws.com/photos/257781612/large.jpeg
  by: Andrew Nunns
  href: https://www.inaturalist.org/observations/149453852
tags: [open data, GBIF]
---

Last week, the Global Biodiversity Information Facility (GBIF) launched their [new awesome data portal](http://www.gbif.org/). One of the things I like most is that the record limit on downloads has been lifted, so we now have free and open access to all 415+ million occurrence records GBIF aggregates. GBIF also makes an effort to lower the barrier to correctly attribute the data publishers, by providing extensive metadata and a citation suggestion in each data download.

That doesn't mean however that it is actually easy to legally use the data, [something GBIF is aware of](/posts/gbif-data-license.html). As a test, I downloaded all [13,297 georeferenced American bullfrog records](http://www.gbif.org/occurrence/search?TAXON_KEY=2427091&HAS_COORDINATE=true&HAS_GEOSPATIAL_ISSUE=false) and would like to visualize and share these on a map using [CartoDB](http://cartodb.com). Technically, this would only take me a few minutes, but to make sure I'm not violating any restrictions, I need to take a closer look at the fine print.

![Unavailable bullfrog records](/assets/images/2013-10-17-illegal-bullfrogs-map-unavailable.png)

## 65 data licenses

By downloading the data from GBIF, I agree with the [data use agreement](http://www.gbif.org/disclaimer/datause), which states among other things: 

> * Users must comply with additional terms and conditions of use set by the Data Publisher. Where these exist they will be available through the metadata associated with the data.

Indeed, GBIF includes metadata for each dataset included in my download, and a file with all the rights as supplied by the data publishers (`rights.txt`). Since my download aggregates records from 65 data publishers, I have to read and understand 65 license statements before I can use the data[^1].

[^1]: Sadly, these licenses are not attached to the data itself (maybe to prevent file size bloat), so I had to manually match (with some help of [Open Refine](http://openrefine.org/)) the metadata with the data using `dataset_id` in order to have the license per record.

### Standard data licenses

Four datasets are provided with a standard data license (e.g. [Creative Commons](http://creativecommons.org/licenses/)) and thus easy to understand:

License | # of datasets | # of records | % of records
--- | ---: | ---: | ---:
[CC0](http://creativecommons.org/publicdomain/zero/1.0/) | 2 ([1](http://www.gbif.org/dataset/8c201186-d997-4b65-aac9-2fcf442a93f6) & [1](http://www.gbif.org/dataset/cc28549b-467f-448c-875e-881ca507aba8)) | 543 | 4%
[CC-BY-SA](http://creativecommons.org/licenses/by-sa/3.0/) | [1](http://www.gbif.org/dataset/b70121ef-b7ea-4316-a05b-abdf30f5ca09) | 4 | 0%
[CC-BY-NC-SA](http://creativecommons.org/licenses/by-sa/3.0/) | [1](http://www.gbif.org/dataset/94dce9c1-e2f0-45cb-a77b-8e5caa871a41) | 1 | 0%
Non-standard license | 61 | 12,749 | 96%

### Interpreting the other licenses

I am entering unknown legal territory by interpreting the non-standard licenses, but since I would like to create an occurrence map with more than 4% of the data, I'll try anyway.

24 datasets don't supply rights, so I could either interpret this as: 1) I'm free to use these data under the general GBIF data use agreement, or 2) I don't want to risk violating any applicable copyright or database rights, so I won't use these data.

I interpreted[^2] other statements as *Non-commercial use* (1 dataset, 22 records), *Non-commercial use with attribution* (5 datasets, 3,190 records), *Public domain* (1 dataset, 1 record) or *All rights reserved* (1 dataset: I'm looking at you, [Royal Belgian Institute for Natural Sciences](http://www.gbif.org/dataset/8138eb72-f762-11e1-a439-00145eb45e9a), 1 record). For 3 datasets (373 records) it was unclear to me what the license allowed.

[^2]: I would like to show you how I interpreted the licenses by posting the data on GitHub, but that would violate some licenses.

The bulk of the data however (26 datasets, 6,894 records) have a license of the form (emphasis mine):

> [Institution A] data records may be used by individual researchers or research groups, but **they may not be repackaged, resold, or redistributed in any form without the express written consent** of a curatorial staff member of [Institution A]. If any of these records are used in an analysis or report, the provenance of the original data must be acknowledged and [Institution A] notified. [Institution A] and its staff are not responsible for damages, injury or loss due to the use of these data.

… or something along the same lines, which I interpreted as *Some use with attribution, no redistribution*.

### Overview of the licenses used

License | # of datasets | # of records | % of records | [GBIF practice?](https://docs.google.com/file/d/0B-PC5KKdhYCQZ1Y5Q2RySmdPbjQ/edit?usp=sharing) | [Open data?](http://opendefinition.org/okd/)
--- | ---: | ---: | ---: | --- | ---
Public domain (incl. CC0) | 3 | 544 | 4% | yes | yes
Use with attribution and share alike (incl. CC-BY-SA) | 1 | 4 | 0% | no | yes
Non-commercial use | 1 | 22 | 0% | expected by some | no
Non-commercial use with attribution (similar to [CC-BY-NC](http://creativecommons.org/licenses/by-nc/3.0/)) | 5 | 3,190 | 24% | expected by some | no 
Non-commercial use with attribution and share alike (incl. CC-BY-NC-SA | 1 | 1 | 0% | no | no
Some use with attribution, no redistribution | 26 | 6,894 | 52% | no | no
All rights reserved | 1 | 1 | 0% | no | no
Unclear | 3 | 373 | 3% | ? | ?
Not supplied | 24 | 2,268 | 17%  | ? | ?

These results are quite bleak: only 4 data publishers (4% of the data) publish their bullfrog occurrences as open data and only 8 (28% of the data) publish their data compatible with practices or expectations in GBIF today. This doesn't even address if the chosen license makes actual sense for data ([see my previous blog post](/posts/gbif-data-license.html)).

## What maps can I show you?

### Public records

![Public bullfrog records](/assets/images/2013-10-17-illegal-bullfrogs-map-public.png)

This map shows all **544 records dedicated to the public domain (4%)**. To comply with the GBIF data use agreement, I must publicly acknowledge the data publishers whose biodiversity data I have used here. I am happy to highlight such open datasets:

* [Herpetology Collection - Royal Ontario Museum](http://www.gbif.org/dataset/8c201186-d997-4b65-aac9-2fcf442a93f6)
* [Colección de anfibios - Museo de Herpetología de la Universidad de Antioquia](http://www.gbif.org/dataset/cc28549b-467f-448c-875e-881ca507aba8)
* [Ministerio de Medio Ambiente, y Medio Rural y Marino. Dirección General de Medio Natural y Política Forestal. Inventario Nacional de Biodiversidad 2007, Anfibios](http://www.gbif.org/dataset/635e4476-f762-11e1-a439-00145eb45e9a), though it would be useful if a standard license was used instead of `Público`.

### Public and non-commercial use records

Since my blog is not ad-supported, I can also include records with a non-commercial use restriction, which adds up to **3,756 records (28%)**. Beware if you want to repost this image.

![Public and non-commercial bullfrog records](/assets/images/2013-10-17-illegal-bullfrogs-map-non-commercial.png)

The included data publishers are now:

> Museum of Vertebrate Zoology, Ministry of Agriculture, Food and Environment, Cornell Lab of Ornithology, Bird Studies Canada, Ohio State University Insect Collection, National Museum of Natural History, Smithsonian Institution, Royal Ontario Museum & Universidad de Antioquia

### All records

I cannot show you [a map](http://www.gbif.org/species/2427091)[^3] including the other 72% of the records, either because the license is incompatible with the other data (such as share alike), but mainly because I first need to contact 52 institutions to either get some clarification of their license or to receive a written consent that I can actually repackage the data as a map. Frankly, that seems quite a hassle for a simple map. And even if I did this, you would have to do the same if you want to use, repackage or redistribute that map as well.

[^3]: So why can GBIF show you the occurrence map that I can't? I believe because of this clause in [their data sharing agreement](http://www.gbif.org/species/2427091): *GBIF Secretariat may cache a copy and serve full or partial data further to other users together with the terms and conditions for use set by the Data Publisher.*

## Conclusion

I just used a small sample of aggregated data[^4], but I hope it demonstrates the unnecessary legal burden that is put on users of the data (note that I haven't even started assessing the data quality or fit for my use). This will either result in less use of the data, or - and I think this is what happens most often - users ignoring the fine print. In both cases, it shows what [I](/posts/gbif-data-license.html) and [others](http://doi.org/10.6084/m9.figshare.799766) have written before:

> A legal license is not the correct tool to enforce or communicate expected data use.

Biodiversity data should be dedicated to the [public domain](http://creativecommons.org/publicdomain/zero/1.0/). Its ethical use should be communicated via community norms.

[^4]: I would love to redo this exercise for all 415+ million occurrences, but that is beyond the scope of what I can do alone, in my free time. Collaborative GitHub project anyone?
