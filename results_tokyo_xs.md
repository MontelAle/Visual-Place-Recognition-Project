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

# <span style="color:green">Task 2: Re-ranking phase phase</span>
| Method | Backbone | Dataset | Metric | Matcher | R@1 | R@5 | R@10 | R@20 | Time |
| :--- | :--- | :--- | :--- | :--- | :---: | :---: | :---: | :---: | :--- |
| netvlad | vgg16 | tokyo_xs | L2 | superpoint-lg | 68.9 | 71.7 | 73.0 | 74.6 | |
| netvlad | vgg16 | tokyo_xs | L2 | superglue | 67.0 | 71.1 | 72.7 | 74.6 | |
| netvlad | vgg16 | tokyo_xs | L2 | loftr | 68.9 | 70.8 | 73.0 | 74.6 | |
| netvlad | vgg16 | sf_xs | L2 | superpoint-lg | 62.5 | 64.7 | 65.0 | 65.3 | |
| netvlad | vgg16 | sf_xs | L2 | superglue | 60.6 | 64.1 | 64.6 | 65.3 | |
| netvlad | vgg16 | sf_xs | L2 | loftr | 61.5 | 63.9 | 64.4 | 65.3 | |
| netvlad | vgg16 | svox_night | L2 | superpoint-lg | 25.0 | 27.5 | 28.4 | 29.5 | |
| netvlad | vgg16 | svox_night | L2 | superglue | 25.0 | 27.3 | 28.7 | 29.5 | |
| netvlad | vgg16 | svox_night | L2 | loftr | 25.5 | 27.6 | 28.9 | 29.5 | |
| netvlad | vgg16 | svox_sun | L2 | superpoint-lg | 65.0 | 66.5 | 67.6 | 69.0 | |
| netvlad | vgg16 | svox_sun | L2 | superglue | 64.2 | 66.4 | 67.8 | 69.0 | |
| netvlad | vgg16 | svox_sun | L2 | loftr | 64.8 | 66.6 | 67.7 | 69.0 | |


| Method | Backbone | Dataset | Metric | Matcher | R@1 | R@5 | R@10 | R@20 | Time |
| :--- | :--- | :--- | :--- | :--- | :---: | :---: | :---: | :---: | :--- |
| netvlad | vgg16 | tokyo_xs | L2 | superpoint-lg | 68.9 | 71.7 | 73.0 | 74.6 | |
| netvlad | vgg16 | tokyo_xs | L2 | superglue | 67.0 | 71.1 | 72.7 | 74.6 | |
| netvlad | vgg16 | tokyo_xs | L2 | loftr | 68.9 | 70.8 | 73.0 | 74.6 | |
| netvlad | vgg16 | sf_xs | L2 | superpoint-lg | 62.5 | 64.7 | 65.0 | 65.3 | |
| netvlad | vgg16 | sf_xs | L2 | superglue | 60.6 | 64.1 | 64.6 | 65.3 | |
| netvlad | vgg16 | sf_xs | L2 | loftr | 61.5 | 63.9 | 64.4 | 65.3 | |
| netvlad | vgg16 | svox_night | L2 | superpoint-lg | 25.0 | 27.5 | 28.4 | 29.5 | |
| netvlad | vgg16 | svox_night | L2 | superglue | 25.0 | 27.3 | 28.7 | 29.5 | |
| netvlad | vgg16 | svox_night | L2 | loftr | 25.5 | 27.6 | 28.9 | 29.5 | |
| netvlad | vgg16 | svox_sun | L2 | superpoint-lg | 65.0 | 66.5 | 67.6 | 69.0 | |
| netvlad | vgg16 | svox_sun | L2 | superglue | 64.2 | 66.4 | 67.8 | 69.0 | |
| netvlad | vgg16 | svox_sun | L2 | loftr | 64.8 | 66.6 | 67.7 | 69.0 | |