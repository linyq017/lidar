%%bash
# step.0. found tiles that overlap with polygons, saved to a list
awk -F " " '{ if(NR>1) printf("%s\n", $4) }' /workspace/Lidardata01/Lin/Data/tiflist_overlap.txt > /workspace/Lidardata01/Lin/Data/laz_overlap_name.txt

# add the ".laz" to the end of the list so it can be read
awk '{ print $1".laz" }' /workspace/Lidardata01/Lin/Data/laz_overlap_name.txt > /workspace/Lidardata01/Lin/Data/laz_overlap_name1.txt

# define the source and destination dirs
source_dir="/workspace/Lidardata01/National_datasets/LiDAR/laserdata_skog"
destination_dir="/workspace/Lidardata01/Lin/Data/overlapping_laz"
file_list="/workspace/Lidardata01/Lin/Data/laz_overlap_name1.txt"

# Create the destination directory if it doesn't exist
mkdir -p "$destination_dir"

# Read the file list and copy the files. The -r option is used with read to preserve leading/trailing whitespaces in file names. IFS= internal field separator. set IFS to an empty value (IFS=), it disables word splitting and treats the entire line, including spaces, as a single field 
while IFS= read -r file_name; do
    # Find the file in the source directory, find goes through the folders recursively
    file_path=$(find "$source_dir" -name "$file_name")

    # Copy the file to the destination directory
    cp "$file_path" "$destination_dir"
done < "$file_list"
