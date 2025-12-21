# <span style="color:green">Task 1: image retrieval phase</span>

| Method   | Backbone | Dataset  | Metric |  R@1 |  R@5 | R@10 | R@20 | Time  |
| -------- | -------- | -------- | ------ | ---: | ---: | ---: | ---: | ----- |
| netvlad  | vgg16    | tokyo_xs | L2     | 54.0 | 64.4 | 69.5 | 74.6 | 06:48 |
| netvlad  | vgg16    | tokyo_xs | cosine | 54.0 | 64.4 | 69.5 | 74.6 | 06:26 |
| mixvpr   | resnet50 | tokyo_xs | L2     | 76.5 | 88.6 | 92.1 | 94.3 | 02:28 |
| mixvpr   | resnet50 | tokyo_xs | cosine | 76.5 | 88.6 | 92.1 | 94.3 | 02:24 |
| megaloc  | dinov2   | tokyo_xs | L2     | 95.6 | 97.8 | 98.7 | 99.0 | 24:08 |
| megaloc  | dinov2   | tokyo_xs | cosine | 95.6 | 97.8 | 98.7 | 99.0 | 22:22 |
| cosplace | resnet50 | tokyo_xs | L2     | 73.3 | 83.8 | 87.9 | 91.4 | 03:58 |
| cosplace | resnet50 | tokyo_xs | cosine | 73.3 | 83.8 | 87.9 | 91.4 | 03:37 |
