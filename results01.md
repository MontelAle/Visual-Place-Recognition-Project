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

# <span style="color:green">Task 2: Re-ranking phase</span>
| Method | Backbone | Dataset | Metric | Matcher | R@1 | R@5 | R@10 | R@20 | Time |
| :--- | :--- | :--- | :--- | :--- | :---: | :---: | :---: | :---: | :--- |
| netvlad | vgg16 | tokyo_xs | L2 | superpoint-lg | 68.9 | 71.7 | 73.0 | 74.6 | 04:46 |
| netvlad | vgg16 | tokyo_xs | L2 | superglue | 67.0 | 71.1 | 72.7 | 74.6 | 04:31 |
| netvlad | vgg16 | tokyo_xs | L2 | loftr | 68.9 | 70.8 | 73.0 | 74.6 | 04:24 |
| netvlad | vgg16 | sf_xs | L2 | superpoint-lg | 62.5 | 64.7 | 65.0 | 65.3 | 15:35 |
| netvlad | vgg16 | sf_xs | L2 | superglue | 60.6 | 64.1 | 64.6 | 65.3 | 15:09 |
| netvlad | vgg16 | sf_xs | L2 | loftr | 61.5 | 63.9 | 64.4 | 65.3 | 14:53 |
| netvlad | vgg16 | svox_sun | L2 | superpoint-lg | 65.0 | 66.5 | 67.6 | 69.0 | 29:15 |
| netvlad | vgg16 | svox_sun | L2 | superglue | 64.2 | 66.4 | 67.8 | 69.0 | 13:15 |
| netvlad | vgg16 | svox_sun | L2 | loftr | 64.8 | 66.6 | 67.7 | 69.0 | 12:31 |
| netvlad | vgg16 | svox_night | L2 | superpoint-lg | 25.0 | 27.5 | 28.4 | 29.5 | 17:30 |
| netvlad | vgg16 | svox_night | L2 | superglue | 25.0 | 27.3 | 28.7 | 29.5 | 12:24 |
| netvlad | vgg16 | svox_night | L2 | loftr | 25.5 | 27.6 | 28.9 | 29.5 | 11:48 |

| Method | Backbone | Dataset | Metric | Matcher | R@1 | R@5 | R@10 | R@20 | Time |
| :--- | :--- | :--- | :--- | :--- | :---: | :---: | :---: | :---: | :--- |
| mixvpr | resnet50 | tokyo_xs | L2 | superpoint-lg | 89.2 | 92.1 | 93.7 | 94.3 | 10:55 |
| mixvpr | resnet50 | tokyo_xs | L2 | superglue | 88.9 | 92.4 | 93.3 | 94.3 | 04:58 |
| mixvpr | resnet50 | tokyo_xs | L2 | loftr | 90.2 | 93.0 | 93.7 | 94.3 | 04:08 |
| mixvpr | resnet50 | sf_xs | L2 | superpoint-lg | 80.5 | 82.5 | 83.2 | 83.6 | 15:59 |
| mixvpr | resnet50 | sf_xs | L2 | superglue | 79.3 | 82.2 | 83.2 | 83.6 | 15:59 |
| mixvpr | resnet50 | sf_xs | L2 | loftr | 79.4 | 82.8 | 83.5 | 83.6 | 13:04 |
| mixvpr | resnet50 | svox_sun | L2 | superpoint-lg | nan | nan | nan | nan | 00:00 |
| mixvpr | resnet50 | svox_sun | L2 | superglue | nan | nan | nan | nan | 00:00 |
| mixvpr | resnet50 | svox_sun | L2 | loftr | nan | nan | nan | nan | 00:00 |
| mixvpr | resnet50 | svox_night | L2 | superpoint-lg | 80.7 | 85.0 | 86.0 | 86.8 | 00:07 |
| mixvpr | resnet50 | svox_night | L2 | superglue | 79.2 | 84.6 | 86.3 | 86.8 | 00:14 |
| mixvpr | resnet50 | svox_night | L2 | loftr | 81.1 | 85.4 | 86.3 | 86.8 | 00:03 |