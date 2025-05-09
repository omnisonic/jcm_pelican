#!/bin/bash

convert_dir="./converted_to_webp"
mkdir -p "$convert_dir" # Ensure the directory exists, creating it if necessary.

for file in *.{JPG,jpg,jpeg,png,webp}; do #  Iterate over all files in this directory.

    # the -short flag to condense printed messege.
    cwebp -short -q 80 "$file" -o "${convert_dir}/${file%.*}.webp" # Convert the image to webp format.
done
