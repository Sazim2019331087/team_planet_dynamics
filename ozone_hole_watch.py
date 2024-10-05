import requests

def download_image(image_url, save_path):
    try:
        # Send a GET request to the image URL
        response = requests.get(image_url)

        # Check if the request was successful
        if response.status_code == 200:
            # Write the content of the response (the image) to a file
            with open(save_path, 'wb') as file:
                file.write(response.content)
            print(f"Image successfully downloaded and saved as {save_path}")
        else:
            print(f"Failed to retrieve the image. Status code: {response.status_code}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage

year = input("Enter Year: ")
month = input("Enter month: ")

north_hem_image_url=f"https://ozonewatch.gsfc.nasa.gov/ozone_maps/images/climate/OZONE_D{year}-{month}_G%5E716X716_PA:TIME.IOMPS_PNPP_V21_MGEOS5FP_LNH.PNG"

south_hem_image_url=f"https://ozonewatch.gsfc.nasa.gov/ozone_maps/images/climate/OZONE_D{year}-{month}_G%5E716X716_PA:TIME.IOMPS_PNPP_V21_MGEOS5FP_LSH.PNG"

north_hem_save_path = f"northern_hemi_sphere_ozone_image_{month}_{year}.png"
south_hem_save_path = f"southern_hemi_sphere_ozone_image_{month}_{year}.png"

download_image(north_hem_image_url, north_hem_save_path)
download_image(south_hem_image_url, south_hem_save_path)

print("False-color view of total ozone over the Arctic pole. The purple and blue colors are where there is the least ozone, and the yellows and reds are where there is more ozone. For more information visit https://ozonewatch.gsfc.nasa.gov/")
