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
