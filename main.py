from typing import Optional
import uvicorn

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

data = [
    {
        "id": 1,
        "name": "Mintwud by Pepperfry - Takai Queen Size Bed in Wenge Finish",
        "image": "https://images-na.ssl-images-amazon.com/images/I/61ut7N7fMVL._SL1210_.jpg",
        "description": "H 31.5 x W 63.3 x D 81.3; Seating Height - 9.2; Mattress Size : 60 x 78 (Not Included) (All dimensions are in inches) \n \
            Room Type: Bedroom \n \
            Pepperfry will arrrange for carpenter service with in 72 hours post delivery. Assembly cost is included in the price of the product. \n \
            Accessories shown in the image are only for representation and are not part of the product. \n \
            Depending on your screen settings and resolution on your device there may be a slight variance in fabric colour and wood polish of the image and actual product."
    },
    {
        "id": 2,
        "name": "CasaCraft by Pepperfry - Adan King Size Bed with Storage in Brown Colour",
        "image": "https://images-na.ssl-images-amazon.com/images/I/71O7XPFOcoL._SL1500_.jpg",
        "description": "H 45.4 x W 108 x D 82; Seating height - 14; Mattress Size-72x78 (Not included)(All dimensions are in inches) \n \
            Room Type: Bedroom \n \
            Pepperfry will arrrange for carpenter service with in 72 hours post delivery. Assembly cost is included in the price of the product. \n \
            Accessories shown in the image are only for representation and are not part of the product. \n \
            Depending on your screen settings and resolution on your device there may be a slight variance in fabric colour and wood polish of the image and actual product."
    },
    {
        "id": 3,
        "name": "Woodsworth by Pepperfry - Segur Solid Wood King Size Bed with Storage in Provincial Teak Finish",
        "image": "https://images-na.ssl-images-amazon.com/images/I/71tp9V1I9hL._SL1500_.jpg",
        "description": "H 39 x W 74 x D 84; Seating Height-15; Mattress Not Included \n \
            Room Type: Bedroom \n \
            Pepperfry will arrrange for carpenter service with in 72 hours post delivery. Assembly cost is included in the price of the product. \n \
            Accessories shown in the image are only for representation and are not part of the product. \n \
            Depending on your screen settings and resolution on your device there may be a slight variance in fabric colour and wood polish of the image and actual product."
    },
    {
        "id": 4,
        "name": "Mintwud by Pepperfry - Toya Queen Size Bed with Storage in Walnut Finish",
        "image": "https://images-na.ssl-images-amazon.com/images/I/71IaYjLqgdL._SL1500_.jpg",
        "description": "H 35.4 x W 63.9 x D 83.9; Seating Height-12; Mattress size : 78 x 60 (Not included) (All dimension in inches) \
            Room Type: Bedroom \
            Pepperfry will arrrange for carpenter service with in 72 hours post delivery. Assembly cost is included in the price of the product. \
            Accessories shown in the image are only for representation and are not part of the product. \
            Depending on your screen settings and resolution on your device there may be a slight variance in fabric colour and wood polish of the image and actual product."
    },
    {
        "id": 5,
        "name": "Canon EOS 1500D 24.1 Digital SLR Camera (Black) with EF S18-55 is II Lens",
        "image": "https://images-na.ssl-images-amazon.com/images/I/914hFeTU2-L._SL1500_.jpg",
        "description": "Sensor: APS-C CMOS Sensor with 24.1 MP (high resolution for large prints and image cropping) \
            ISO: 100-6400 sensitivity range (critical for obtaining grain-free pictures, especially in low light) \
            Image Processor: DIGIC 4+ with 9 autofocus points (important for speed and accuracy of autofocus and burst photography) \
            Video Resolution: Full HD video with fully manual control and selectable frame rates (great for precision and high-quality video work) \
            Connectivity: WiFi, NFC and Bluetooth built-in (useful for remotely controlling your camera and transferring pictures wirelessly as you shoot) \
            Lens Mount: EF-S mount compatible with all EF and EF-S lenses (crop-sensor mount versatile and compact, especially when used with EF-S lenses) \
            For any queries, please contact_us on: [1860-180-3366] \
            Country of Origin: Taiwan"
    },

    {
        "id": 6,
        "name": "Canon PowerShot SX540HS 20.3MP Digital Camera with 50x Optical Zoom (Black)",
        "image": "https://images-na.ssl-images-amazon.com/images/I/71Xp-K4MMBL._SL1000_.jpg",
        "description": "Sensor: APS-C CMOS sensor with 20.3 MP (high resolution for large prints and image cropping) \
            ISO: 80-3200 sensitivity range (critical for obtaining grain-free pictures, especially in low light) \
            Image Processor: DIGIC 6 with 1 autofocus points (important for speed and accuracy of autofocus and burst photography) \
            Video Resolution: HD video with fully manual control and selectable frame rates \
            Connectivity: WiFi, NFC and Bluetooth built-in (useful for remotely controlling your camera and transferring pictures wirelessly as you shoot) \
            Lens Mount: EF-S mount compatible with all EF and EF-S lenses (crop-sensor mount versatile and compact, especially when used with EF-S lenses)"
    },
    {
        "id": 7,
        "name": "Canon EOS 80D 24.2MP Digital SLR Camera (Black) + EF-S 18-135mm f/3.5-5.6 Image Stabilization USM Lens Kit",
        "image": "https://images-na.ssl-images-amazon.com/images/I/61VFkA-rceL._SL1000_.jpg",
        "description": "Sensor: APS-C CMOS Sensor with 24.2 MP (high resolution for large prints and image cropping) \
            ISO: 100-12800 sensitivity range (critical for obtaining grain-free pictures, especially in low light) \
            Image Processor: DIGIC 6 with 45 autofocus points (important for speed and accuracy of autofocus and burst photography) \
            Video Resolution: Full HD video with fully manual control and selectable frame rates (great for precision and high-quality video work) \
            Connectivity: WiFi, NFC and Bluetooth built-in (useful for remotely controlling your camera and transferring pictures wirelessly as you shoot) \
            Lens Mount: EF-S mount compatible with all EF and EF-S lenses (crop-sensor mount versatile and compact, especially when used with EF-S lenses) \
            A responsive camera to keep pace with the action"
    },
    {
        "id": 8,
        "name": "Unique Carpet Floral Persian Carpet (Blue, Wool And Wool Blend, 4 X 6)",
        "image": "https://images-na.ssl-images-amazon.com/images/I/819QwHB7CcL._SL1500_.jpg",
        "description": "Construction: Hand tufted, Durable cotton canvas backing \
            Material: Wool,Pile Height: 1 Inches \
            Hand Woven with Fine Wool in Master Designed By Well Versed Weaver \
            Exquisite Color Combination , Binding on Edge , Canvas Backing With Best Quality"
    },
    {
        "id": 9,
        "name": "Sifa Carpet Export Quality Hand Woven-5x8 Feet Pure Wool Tufted Carpet for Your Living Room with 1.5 Inch Pile Height (150x240CM Multi Color)",
        "image": "https://images-na.ssl-images-amazon.com/images/I/91ZMJ9qRQML._SL1500_.jpg",
        "description": "Super Softness With Anti Skid Carpet \
            If You have Querry Different Colour and Different Size .Plz Click on (Sifa Carpet)Top Of This Listing and Plz Write on Sifa Carpet on Search Bar \
            Wash Care - Easy Wash with Cold Ditergent Water \
            To Make The Product Better Binding On Edge and Canvas Backing Has Been Used \
            High Quality with 1.5 Inch Pile Height"
    },
    {
        "id": 10,
        "name": "Rahman Carpets Handwoven Super Modern Shag Area Silky Smooth Rugs Fluffy Rugs Anti-Skid Shaggy Area Rug, Bedroom Carpet 4 x 6 feet (120X180 cm) Multi",
        "image": "https://images-na.ssl-images-amazon.com/images/I/91UXstTm3AL._SL1500_.jpg",
        "description": "Hand Woven Shaggy Carpet with Fine Microfiber Wool in Master Designed By Well Versed Weaver \
            Contemporary shag style works beautifully with any décor and Extra thick 1.5 inch pile height provides exceptional sink-in comfort \
            Care instructions: Vacuum Regularly For Cleaning Spot. This Rug is Stain And Fade Resistant \
            Exquisite Color Combination , Binding on Edge , Canvas Backing With Best Quality , Contemporary shag style works beautifully with any décor . \
            Rahman Carpets has been a trusted brand in home furnishings for over 10 years, providing quality craftsmanship and unmatched style."
    },


]


@app.get("/api/v1/search")
def search(query: str):
    searchResult = []
    for i in data:
        if(query.lower() in i["name"].lower() or query.lower() in i["description"].lower()):
            searchResult.append(i)

    return {"data": searchResult}

if __name__ == "__main__":
    uvicorn.run(app, host='0.0.0.0')