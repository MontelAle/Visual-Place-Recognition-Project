# Task 1

| Method  | Backbone | Dataset | Metric |  R@1 |  R@5 | R@10 | R@20 | Time  |
| ------- | -------- | ------- | ------ | ---: | ---: | ---: | ---: | ----- |
| netvlad | vgg16    | sf_xs   | L2     | 42.2 | 53.7 | 60.8 | 65.3 |       |
| netvlad | vgg16    | sf_xs   | cosine | 42.2 | 53.7 | 60.8 | 65.3 | 12:54 |
| mixvpr  | resnet50 | sf_xs   | L2     |      |      |      |      |       |
