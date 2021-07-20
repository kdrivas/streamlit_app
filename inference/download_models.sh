BASE_URL="http://cs.stanford.edu/people/jcjohns/fast-neural-style/models/"

mkdir models

wget "$BASE_URL/instance_norm/mosaic.t7" -c -O 'models/mosaic.t7'
wget "$BASE_URL/instance_norm/candy.t7" -c -O 'models/candy.t7'
wget "$BASE_URL/instance_norm/la_muse.t7" -c -O 'models/la_muse.t7'
wget "$BASE_URL/instance_norm/feathers.t7" -c -O 'models/feathers.t7'
wget "$BASE_URL/instance_norm/the_scream.t7" -c -O 'models/the_scream.t7'
wget "$BASE_URL/instance_norm/udnie.t7" -c -O 'models/udnie.t7'
wget "$BASE_URL/eccv16/composition_vii.t7" -c -O 'models/composition_vii.t7'
