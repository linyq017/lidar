import whitebox
import argparse
import os
import glob

whitebox.download_wbt(linux_musl=True, reset=True)
wbt = whitebox.WhiteboxTools()

def laz_to_dem(laz_dir, resolution):
    """
    converts all laz tiles in a directory to a digital elevation raster.
    """  
    wbt.set_verbose_mode(True)
    wbt.set_working_dir(laz_dir)
    
    for f in os.listdir(laz_dir):
        if f.endswith('.laz'):
            laz_file = os.path.join(laz_dir, f)
            tif_file = os.path.join(laz_dir, f.replace('.laz', '.tif'))
            
            if not os.path.exists(tif_file):# check if laz already has a corresponding tif, if so, skip lidar tin gridding
                wbt.lidar_tin_gridding(parameter="elevation", 
                                       returns="last",
                                       resolution=resolution,
                                       exclude_cls="0,1,3,4,5,6,7,8,10,11,12,13,14,15,16,17,18",
                                       minz=None,
                                       maxz=None,
                                       max_triangle_edge_length=50,
                                       i=laz_file
                                      )
                print("Completed TIN interpolation for:", f)

    print("Completed TIN interpolation\n")

def fill_holes(dem_img, dem_fill):
    wbt.fill_missing_data(
        i=dem_img, 
        output=dem_fill, 
        filter=5000, 
        weight=2.0, 
        no_edges=False
    )

def main(laz_dir, dem_dir, resolution):
    laz_to_dem(laz_dir, resolution)

    for f in os.listdir(laz_dir):
        if f.endswith('.tif'):
            dem_img = os.path.join(laz_dir, f)
            dem_fill = os.path.join(dem_dir, f)
            fill_holes(dem_img, dem_fill)
            os.remove(dem_img)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Select the lidar tiles which contains training data',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('laz_dir', help='Path to directory where laz files are stored')   
    parser.add_argument('dem_dir', help='Path to directory where dem files are stored')  
    parser.add_argument('resolution', type=float, help='set output dem resolution in meters')
    args = vars(parser.parse_args())
    main(**args)
