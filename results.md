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

| Method   | Backbone | Dataset    | Metric |  R@1 |  R@5 | R@10 | R@20 | Time  |
| -------- | -------- | ---------- | ------ | ---: | ---: | ---: | ---- | ----- |
| netvlad  | vgg16    | svox_night | L2     |  8.5 | 18.2 | 22.7 | 29.5 | 04:39 |
| netvlad  | vgg16    | svox_night | cosine |  8.5 | 18.2 | 22.7 | 29.5 | 04:45 |
| mixvpr   | resnet50 | svox_night | L2     | 62.6 | 80.2 | 83.7 | 87.4 | 01:21 |
| mixvpr   | resnet50 | svox_night | cosine | 62.6 | 80.2 | 83.7 | 87.4 | 01:18 |
| megaloc  | dinov2   | svox_night | L2     | 96.5 | 98.7 | 99.0 | 99.3 | 13:17 |
| megaloc  | dinov2   | svox_night | cosine | 96.5 | 98.7 | 99.0 | 99.3 | 13:25 |
| cosplace | resnet50 | svox_night | L2     | 49.2 | 66.1 | 72.8 | 78.6 | 02:39 |
| cosplace | resnet50 | svox_night | cosine | 49.2 | 66.1 | 72.8 | 78.6 | 02:45 |

| Method   | Backbone | Dataset  | Metric |  R@1 |  R@5 | R@10 | R@20 | Time  |
| -------- | -------- | -------- | ------ | ---: | ---: | ---: | ---- | ----- |
| netvlad  | vgg16    | svox_sun | L2     | 37.1 | 54.4 | 62.2 | 69.0 | 04:39 |
| netvlad  | vgg16    | svox_sun | cosine | 37.1 | 54.4 | 62.2 | 69.0 | 04:45 |
| mixvpr   | resnet50 | svox_sun | L2     | 84.4 | 92.7 | 94.6 | 95.4 | 01:21 |
| mixvpr   | resnet50 | svox_sun | cosine | 84.4 | 92.7 | 94.6 | 95.4 | 01:18 |
| megaloc  | dinov2   | svox_sun | L2     | 97.2 | 99.3 | 99.5 | 99.6 | 13:17 |
| megaloc  | dinov2   | svox_sun | cosine | 97.2 | 99.3 | 99.5 | 99.6 | 13:25 |
| cosplace | resnet50 | svox_sun | L2     | 76.9 | 89.0 | 92.4 | 95.0 | 02:38 |
| cosplace | resnet50 | svox_sun | cosine | 76.9 | 89.0 | 92.4 | 95.0 | 02:45 |

# Task 2

| Method   | Backbone | Dataset    | Metric | Matcher       |  R@1 |  R@5 | R@10 | R@20 | Time     |
| -------- | -------- | ---------- | ------ | ------------- | ---: | ---: | ---: | ---: | -------- |
| cosplace | resnet50 | tokyo_xs   | L2     | superpoint-lg | 86.0 | 89.2 | 89.8 | 91.4 | 18:42    |
| cosplace | resnet50 | tokyo_xs   | L2     | superglue     | 84.8 | 88.6 | 90.2 | 91.4 | 07:31    |
| cosplace | resnet50 | tokyo_xs   | L2     | loftr         | 86.7 | 89.2 | 90.5 | 91.4 | 19:39    |
| cosplace | resnet50 | sf_xs      | L2     | superpoint-lg | 82.5 | 85.6 | 86.3 | 86.9 | 01:01:14 |
| cosplace | resnet50 | sf_xs      | L2     | superglue     | 81.5 | 84.9 | 86.3 | 86.9 | 24:15    |
| cosplace | resnet50 | sf_xs      | L2     | loftr         | 81.7 | 84.7 | 86.1 | 86.9 | 01:04:36 |
| cosplace | resnet50 | svox_night | L2     | superpoint-lg | 71.8 | 75.8 | 76.9 | 78.6 | 24:39    |
| cosplace | resnet50 | svox_night | L2     | superglue     | 71.3 | 75.9 | 77.5 | 78.6 | 15:56    |
| cosplace | resnet50 | svox_night | L2     | loftr         | 72.9 | 76.9 | 77.9 | 78.6 | 24:16    |
| cosplace | resnet50 | svox_sun   | L2     | superpoint-lg | 90.2 | 93.6 | 94.6 | 95.0 | 25:42    |
| cosplace | resnet50 | svox_sun   | L2     | superglue     | 86.7 | 93.0 | 94.1 | 95.0 | 16:32    |
| cosplace | resnet50 | svox_sun   | L2     | loftr         | 92.3 | 93.9 | 94.4 | 95.0 | 25:08    |

| Method  | Backbone | Dataset    | Metric | Matcher       |  R@1 |  R@5 | R@10 | R@20 | Time     |
| ------- | -------- | ---------- | ------ | ------------- | ---: | ---: | ---: | ---: | -------- |
| megaloc | dinov2   | tokyo_xs   | L2     | superpoint-lg | 94.3 | 98.4 | 98.7 | 99.0 | 18:54    |
| megaloc | dinov2   | tokyo_xs   | L2     | superglue     | 93.0 | 98.1 | 98.4 | 99.0 | 07:48    |
| megaloc | dinov2   | tokyo_xs   | L2     | loftr         | 94.3 | 97.8 | 98.7 | 99.0 | 20:01    |
| megaloc | dinov2   | sf_xs      | L2     | superpoint-lg | 87.0 | 90.6 | 91.3 | 91.5 | 59:33    |
| megaloc | dinov2   | sf_xs      | L2     | superglue     | 85.8 | 89.9 | 90.7 | 91.5 | 23:24    |
| megaloc | dinov2   | sf_xs      | L2     | loftr         | 86.5 | 89.7 | 90.8 | 91.5 | 01:03:17 |
| megaloc | dinov2   | svox_night | L2     | superpoint-lg | 90.9 | 97.4 | 98.7 | 99.3 | 24:42    |
| megaloc | dinov2   | svox_night | L2     | superglue     | 90.4 | 97.8 | 98.5 | 99.3 | 15:52    |
| megaloc | dinov2   | svox_night | L2     | loftr         | 93.1 | 98.7 | 99.0 | 99.3 | 24:06    |
| megaloc | dinov2   | svox_sun   | L2     | superpoint-lg | 95.8 | 98.9 | 99.4 | 99.6 | 25:22    |
| megaloc | dinov2   | svox_sun   | L2     | superglue     | 94.1 | 98.5 | 99.3 | 99.6 | 16:20    |
| megaloc | dinov2   | svox_sun   | L2     | loftr         | 97.1 | 99.3 | 99.5 | 99.6 | 24:32    |
