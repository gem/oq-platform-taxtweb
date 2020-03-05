#!/bin/bash
fin=$1
fot=$2

IFS='
'
cp "$fot" "taxonomy_morphed.sql"
for r in $(cat $fin); do
    url=$(echo "$r" | sed 's@.*|/terms/@@g')
    echo "$url"
    new_url="$(echo "$url" | sed 's/--/-/g')"
    sed -i "s/$url/$new_url/g" "taxonomy_morphed.sql"
done
