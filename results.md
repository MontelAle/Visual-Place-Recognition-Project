# Task 1

| Method   | Backbone | Dataset | Metric |  R@1 |  R@5 | R@10 | R@20 | Time  |
| -------- | -------- | ------- | ------ | ---: | ---: | ---: | ---: | ----- |
| netvlad  | vgg16    | sf_xs   | L2     | 42.2 | 53.7 | 60.8 | 65.3 | 13:02 |
| netvlad  | vgg16    | sf_xs   | cosine | 42.2 | 53.7 | 60.8 | 65.3 | 12:54 |
| mixvpr   | resnet50 | sf_xs   | L2     | 69.6 | 78.7 | 81.1 | 83.6 | 04:51 |
| mixvpr   | resnet50 | sf_xs   | cosine | 69.6 | 78.7 | 81.1 | 83.6 | 04:44 |
| megaloc  | dinov2   | sf_xs   | L2     | 86.9 | 90.4 | 91.2 | 91.5 | 46:28 |
| megaloc  | dinov2   | sf_xs   | cosine | 86.9 | 90.4 | 91.2 | 91.5 | 45:37 |
| cosplace | resnet50 | sf_xs   | L2     | 70.9 | 80.0 | 84.0 | 86.9 | 07:20 |
| cosplace | resnet50 | sf_xs   | cosine | 70.9 | 80.0 | 84.0 | 86.9 | 07:19 |

| Method  | Backbone | Dataset | Metric |  R@1 |  R@5 | R@10 | R@20 |  Time |
| ------- | -------- | ------- | ------ | ---: | ---: | ---: | ---: | ----: |
| netvlad | vgg16    | svox    | L2     | 86.6 | 93.7 | 95.5 | 96.9 | 43:03 |
| netvlad | vgg16    | svox    | cosine | 86.6 | 93.7 | 95.5 | 96.9 | 43:10 |
| mixvpr  | resnet50 | svox    | L2     | 97.8 | 98.9 | 99.2 | 99.3 | 42:22 |
| mixvpr  | resnet50 | svox    | cosine | 97.8 | 98.9 | 99.2 | 99.3 | 44:27 |
| megaloc | dinov2   | svox    | L2     | 98.7 | 99.5 | 99.6 | 99.7 | 44:28 |
| megaloc | dinov2   | svox    | cosine | 98.7 | 99.5 | 99.6 | 99.7 | 44:56 |
