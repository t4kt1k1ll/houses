from django.db import models

# Create your models here.

class Tm_rental_listings(models.Model):
    ListingId = models.IntegerField(null=True)
    Address = models.CharField(max_length=255, null=True)
    AdjacentSuburbIds_0 = models.IntegerField(null=True)
    AdjacentSuburbIds_1 = models.IntegerField(null=True)
    AdjacentSuburbIds_10 = models.IntegerField(null=True)
    AdjacentSuburbIds_11 = models.IntegerField(null=True)
    AdjacentSuburbIds_12 = models.IntegerField(null=True)
    AdjacentSuburbIds_13 = models.IntegerField(null=True)
    AdjacentSuburbIds_14 = models.IntegerField(null=True)
    AdjacentSuburbIds_2 = models.IntegerField(null=True)
    AdjacentSuburbIds_3 = models.IntegerField(null=True)
    AdjacentSuburbIds_4 = models.IntegerField(null=True)
    AdjacentSuburbIds_5 = models.IntegerField(null=True)
    AdjacentSuburbIds_6 = models.IntegerField(null=True)
    AdjacentSuburbIds_7 = models.IntegerField(null=True)
    AdjacentSuburbIds_8 = models.IntegerField(null=True)
    AdjacentSuburbIds_9 = models.IntegerField(null=True)
    AdjacentSuburbNames_0 = models.CharField(max_length=50, null=True)
    AdjacentSuburbNames_1 = models.CharField(max_length=50, null=True)
    AdjacentSuburbNames_10 = models.CharField(max_length=50, null=True)
    AdjacentSuburbNames_11 = models.CharField(max_length=50, null=True)
    AdjacentSuburbNames_12 = models.CharField(max_length=50, null=True)
    AdjacentSuburbNames_13 = models.CharField(max_length=50, null=True)
    AdjacentSuburbNames_14 = models.CharField(max_length=50, null=True)
    AdjacentSuburbNames_2 = models.CharField(max_length=50, null=True)
    AdjacentSuburbNames_3 = models.CharField(max_length=50, null=True)
    AdjacentSuburbNames_4 = models.CharField(max_length=50, null=True)
    AdjacentSuburbNames_5 = models.CharField(max_length=50, null=True)
    AdjacentSuburbNames_6 = models.CharField(max_length=50, null=True)
    AdjacentSuburbNames_7 = models.CharField(max_length=50, null=True)
    AdjacentSuburbNames_8 = models.CharField(max_length=50, null=True)
    AdjacentSuburbNames_9 = models.CharField(max_length=50, null=True)
    Agency = models.CharField(max_length=50, null=True)
    AgencyReference = models.CharField(max_length=50, null=True)
    Agency_Agents_0_FullName = models.CharField(max_length=100, null=True)
    Agency_Agents_0_MobilePhoneNumber = models.CharField(max_length=20, null=True)
    Agency_Agents_0_OfficePhoneNumber = models.CharField(max_length=20, null=True)
    Agency_Agents_0_Photo = models.CharField(max_length=255, null=True)
    Agency_Agents_0_UrlSlug = models.CharField(max_length=50, null=True)
    Agency_Agents_1_FullName = models.CharField(max_length=100, null=True)
    Agency_Agents_1_MobilePhoneNumber = models.CharField(max_length=20, null=True)
    Agency_Agents_1_OfficePhoneNumber = models.CharField(max_length=20, null=True)
    Agency_Agents_1_Photo = models.CharField(max_length=255, null=True)
    Agency_Agents_1_UrlSlug = models.CharField(max_length=50, null=True)
    Agency_Branding_BackgroundColor = models.CharField(max_length=7, null=True)
    Agency_Branding_DisableBanner = models.NullBooleanField(null=True)
    Agency_Branding_LargeBannerURL = models.CharField(max_length=255, null=True)
    Agency_Branding_OfficeLocation = models.CharField(max_length=100, null=True)
    Agency_Branding_StrokeColor = models.CharField(max_length=7, null=True)
    Agency_Branding_TextColor = models.CharField(max_length=7, null=True)
    Agency_FaxNumber = models.CharField(max_length=20, null=True)
    Agency_Id = models.IntegerField(null=True)
    Agency_IsLicensedPropertyAgency = models.NullBooleanField(null=True)
    Agency_IsRealEstateAgency = models.NullBooleanField(null=True)
    Agency_Logo = models.CharField(max_length=255, null=True)
    Agency_Logo2 = models.CharField(max_length=255, null=True)
    Agency_Name = models.CharField(max_length=255, null=True)
    Agency_PhoneNumber = models.CharField(max_length=20, null=True)
    Agency_Website = models.CharField(max_length=255, null=True)
    Amenities = models.CharField(max_length=255, null=True)
    AsAt = models.CharField(max_length=21, null=True)
    AvailableFrom = models.CharField(max_length=50, null=True)
    Bathrooms = models.SmallIntegerField(null=True)
    Bedrooms = models.SmallIntegerField(null=True)
    BestContactTime = models.CharField(max_length=50, null=True)
    Category = models.CharField(max_length=15, null=True)
    CategoryPath = models.CharField(max_length=255, null=True)
    District = models.CharField(max_length=50, null=True)
    DistrictId = models.SmallIntegerField(null=True)
    EndDate = models.CharField(max_length=21, null=True)
    GeographicLocation_Accuracy = models.SmallIntegerField(null=True)
    GeographicLocation_Easting = models.DecimalField(max_digits=15, decimal_places=10, null=True)
    GeographicLocation_Latitude = models.DecimalField(max_digits=15, decimal_places=10, null=True)
    GeographicLocation_Longitude = models.DecimalField(max_digits=15, decimal_places=10, null=True)
    GeographicLocation_Northing = models.DecimalField(max_digits=15, decimal_places=10, null=True)
    HasEmbeddedVideo = models.NullBooleanField(null=True)
    HasGallery = models.NullBooleanField(null=True)
    IdealTenant = models.CharField(max_length=255, null=True)
    IsBold = models.NullBooleanField(null=True)
    IsClassified = models.NullBooleanField(null=True)
    IsFeatured = models.NullBooleanField(null=True)
    IsHighlighted = models.NullBooleanField(null=True)
    IsSuperFeatured = models.NullBooleanField(null=True)
    ListingGroup = models.CharField(max_length=25, null=True)
    ListingLength = models.NullBooleanField(null=True)
    MaxTenants = models.DecimalField(max_digits=15, decimal_places=10, null=True)
    NoteDate = models.CharField(max_length=25, null=True)
    Parking = models.CharField(max_length=255, null=True)
    PetsOkay = models.DecimalField(max_digits=15, decimal_places=10, null=True)
    PhotoUrls_0 = models.CharField(max_length=255, null=True)
    PhotoUrls_1 = models.CharField(max_length=255, null=True)
    PhotoUrls_10 = models.CharField(max_length=255, null=True)
    PhotoUrls_11 = models.CharField(max_length=255, null=True)
    PhotoUrls_12 = models.CharField(max_length=255, null=True)
    PhotoUrls_13 = models.CharField(max_length=255, null=True)
    PhotoUrls_14 = models.CharField(max_length=255, null=True)
    PhotoUrls_15 = models.CharField(max_length=255, null=True)
    PhotoUrls_16 = models.CharField(max_length=255, null=True)
    PhotoUrls_17 = models.CharField(max_length=255, null=True)
    PhotoUrls_18 = models.CharField(max_length=255, null=True)
    PhotoUrls_2 = models.CharField(max_length=255, null=True)
    PhotoUrls_3 = models.CharField(max_length=255, null=True)
    PhotoUrls_4 = models.CharField(max_length=255, null=True)
    PhotoUrls_5 = models.CharField(max_length=255, null=True)
    PhotoUrls_6 = models.CharField(max_length=255, null=True)
    PhotoUrls_7 = models.CharField(max_length=255, null=True)
    PhotoUrls_8 = models.CharField(max_length=255, null=True)
    PhotoUrls_9 = models.CharField(max_length=255, null=True)
    PictureHref = models.CharField(max_length=255, null=True)
    PriceDisplay = models.CharField(max_length=50, null=True)
    PropertyId = models.CharField(max_length=20, null=True)
    PropertyType = models.CharField(max_length=20, null=True)
    Region = models.CharField(max_length=50, null=True)
    RegionId = models.SmallIntegerField(null=True)
    RentPerWeek = models.IntegerField(null=True)
    ReserveState = models.SmallIntegerField(null=True)
    SmokersOkay = models.FloatField(null=True)
    StartDate = models.CharField(max_length=21, null=True)
    StartPrice = models.IntegerField(null=True)
    Suburb = models.CharField(max_length=50, null=True)
    SuburbId = models.IntegerField(null=True)
    Title = models.CharField(max_length=100, null=True)
    Whiteware = models.CharField(max_length=255, null=True)
    job_run_datetime = models.DateTimeField(null=True)

class Tm_residential_listings(models.Model):
    ListingId = models.IntegerField(null=True)
    Address = models.CharField(max_length=255, null=True)
    AdjacentSuburbIds_0 = models.IntegerField(null=True)
    AdjacentSuburbIds_1 = models.IntegerField(null=True)
    AdjacentSuburbIds_10 = models.IntegerField(null=True)
    AdjacentSuburbIds_11 = models.IntegerField(null=True)
    AdjacentSuburbIds_12 = models.IntegerField(null=True)
    AdjacentSuburbIds_13 = models.IntegerField(null=True)
    AdjacentSuburbIds_14 = models.IntegerField(null=True)
    AdjacentSuburbIds_2 = models.IntegerField(null=True)
    AdjacentSuburbIds_3 = models.IntegerField(null=True)
    AdjacentSuburbIds_4 = models.IntegerField(null=True)
    AdjacentSuburbIds_5 = models.IntegerField(null=True)
    AdjacentSuburbIds_6 = models.IntegerField(null=True)
    AdjacentSuburbIds_7 = models.IntegerField(null=True)
    AdjacentSuburbIds_8 = models.IntegerField(null=True)
    AdjacentSuburbIds_9 = models.IntegerField(null=True)
    AdjacentSuburbNames_0 = models.CharField(max_length=50, null=True)
    AdjacentSuburbNames_1 = models.CharField(max_length=50, null=True)
    AdjacentSuburbNames_10 = models.CharField(max_length=50, null=True)
    AdjacentSuburbNames_11 = models.CharField(max_length=50, null=True)
    AdjacentSuburbNames_12 = models.CharField(max_length=50, null=True)
    AdjacentSuburbNames_13 = models.CharField(max_length=50, null=True)
    AdjacentSuburbNames_14 = models.CharField(max_length=50, null=True)
    AdjacentSuburbNames_2 = models.CharField(max_length=50, null=True)
    AdjacentSuburbNames_3 = models.CharField(max_length=50, null=True)
    AdjacentSuburbNames_4 = models.CharField(max_length=50, null=True)
    AdjacentSuburbNames_5 = models.CharField(max_length=50, null=True)
    AdjacentSuburbNames_6 = models.CharField(max_length=50, null=True)
    AdjacentSuburbNames_7 = models.CharField(max_length=50, null=True)
    AdjacentSuburbNames_8 = models.CharField(max_length=50, null=True)
    AdjacentSuburbNames_9 = models.CharField(max_length=50, null=True)
    Agency = models.NullBooleanField(null=True)
    AgencyReference = models.CharField(max_length=50, null=True)
    Agency_Agents_0_FullName = models.CharField(max_length=100, null=True)
    Agency_Agents_0_MobilePhoneNumber = models.CharField(max_length=20, null=True)
    Agency_Agents_0_OfficePhoneNumber = models.CharField(max_length=20, null=True)
    Agency_Agents_0_Photo = models.CharField(max_length=255, null=True)
    Agency_Agents_0_UrlSlug = models.CharField(max_length=50, null=True)
    Agency_Agents_1_FullName = models.CharField(max_length=100, null=True)
    Agency_Agents_1_MobilePhoneNumber = models.CharField(max_length=20, null=True)
    Agency_Agents_1_OfficePhoneNumber = models.CharField(max_length=20, null=True)
    Agency_Agents_1_Photo = models.CharField(max_length=255, null=True)
    Agency_Agents_1_UrlSlug = models.CharField(max_length=50, null=True)
    Agency_Branding_BackgroundColor = models.CharField(max_length=7, null=True)
    Agency_Branding_DisableBanner = models.NullBooleanField(null=True)
    Agency_Branding_LargeBannerURL = models.CharField(max_length=255, null=True)
    Agency_Branding_OfficeLocation = models.CharField(max_length=100, null=True)
    Agency_Branding_StrokeColor = models.CharField(max_length=7, null=True)
    Agency_Branding_TextColor = models.CharField(max_length=7, null=True)
    Agency_FaxNumber = models.CharField(max_length=20, null=True)
    Agency_Id = models.IntegerField(null=True)
    Agency_IsLicensedPropertyAgency = models.NullBooleanField(null=True)
    Agency_IsRealEstateAgency = models.NullBooleanField(null=True)
    Agency_Logo = models.CharField(max_length=255, null=True)
    Agency_Logo2 = models.CharField(max_length=255, null=True)
    Agency_Name = models.CharField(max_length=255, null=True)
    Agency_PhoneNumber = models.CharField(max_length=20, null=True)
    Agency_Website = models.CharField(max_length=255, null=True)
    Amenities = models.CharField(max_length=255, null=True)
    AsAt = models.CharField(max_length=21, null=True)
    Bathrooms = models.FloatField(null=True)
    Bedrooms = models.FloatField(null=True)
    BestContactTime = models.CharField(max_length=50, null=True)
    Category = models.CharField(max_length=15, null=True)
    CategoryPath = models.CharField(max_length=255, null=True)
    District = models.CharField(max_length=50, null=True)
    DistrictId = models.SmallIntegerField(null=True)
    EndDate = models.CharField(max_length=21, null=True)
    GeographicLocation_Accuracy = models.FloatField(null=True)
    GeographicLocation_Easting = models.FloatField(null=True)
    GeographicLocation_Latitude = models.FloatField(null=True)
    GeographicLocation_Longitude = models.FloatField(null=True)
    GeographicLocation_Northing = models.FloatField(null=True)
    HasEmbeddedVideo = models.NullBooleanField(null=True)
    HasGallery = models.NullBooleanField(null=True)
    IsBold = models.NullBooleanField(null=True)
    IsClassified = models.NullBooleanField(null=True)
    IsFeatured = models.NullBooleanField(null=True)
    IsHighlighted = models.NullBooleanField(null=True)
    IsSuperFeatured = models.NullBooleanField(null=True)
    ListingGroup = models.CharField(max_length=25, null=True)
    ListingLength = models.NullBooleanField(null=True)
    NoteDate = models.CharField(max_length=25, null=True)
    Parking = models.CharField(max_length=255, null=True)
    PhotoUrls_0 = models.CharField(max_length=255, null=True)
    PhotoUrls_1 = models.CharField(max_length=255, null=True)
    PhotoUrls_10 = models.CharField(max_length=255, null=True)
    PhotoUrls_11 = models.CharField(max_length=255, null=True)
    PhotoUrls_12 = models.CharField(max_length=255, null=True)
    PhotoUrls_13 = models.CharField(max_length=255, null=True)
    PhotoUrls_14 = models.CharField(max_length=255, null=True)
    PhotoUrls_15 = models.CharField(max_length=255, null=True)
    PhotoUrls_16 = models.CharField(max_length=255, null=True)
    PhotoUrls_17 = models.CharField(max_length=255, null=True)
    PhotoUrls_18 = models.CharField(max_length=255, null=True)
    PhotoUrls_2 = models.CharField(max_length=255, null=True)
    PhotoUrls_3 = models.CharField(max_length=255, null=True)
    PhotoUrls_4 = models.CharField(max_length=255, null=True)
    PhotoUrls_5 = models.CharField(max_length=255, null=True)
    PhotoUrls_6 = models.CharField(max_length=255, null=True)
    PhotoUrls_7 = models.CharField(max_length=255, null=True)
    PhotoUrls_8 = models.CharField(max_length=255, null=True)
    PhotoUrls_9 = models.CharField(max_length=255, null=True)
    PictureHref = models.CharField(max_length=255, null=True)
    PriceDisplay = models.CharField(max_length=50, null=True)
    PropertyId = models.CharField(max_length=20, null=True)
    PropertyType = models.CharField(max_length=20, null=True)
    Region = models.CharField(max_length=50, null=True)
    RegionId = models.SmallIntegerField(null=True)
    ReserveState = models.SmallIntegerField(null=True)
    StartDate = models.CharField(max_length=21, null=True)
    StartPrice = models.IntegerField(null=True)
    Suburb = models.CharField(max_length=50, null=True)
    SuburbId = models.IntegerField(null=True)
    Title = models.CharField(max_length=100, null=True)
    job_run_datetime = models.CharField(max_length=26, null=True)
    Agency_Agents_0_EMail = models.CharField(max_length=50, null=True)
    Agency_IsJobAgency = models.NullBooleanField(null=True)
    Area = models.FloatField(null=True)
    IsBoosted = models.NullBooleanField(null=True)
    LandArea = models.FloatField(null=True)
    OpenHomes_0_End = models.CharField(max_length=21, null=True)
    OpenHomes_0_Start = models.CharField(max_length=21, null=True)
    OpenHomes_1_End = models.CharField(max_length=21, null=True)
    OpenHomes_1_Start = models.CharField(max_length=21, null=True)
    OpenHomes_2_End = models.CharField(max_length=21, null=True)
    OpenHomes_2_Start = models.CharField(max_length=21, null=True)
    OpenHomes_3_End = models.CharField(max_length=21, null=True)
    OpenHomes_3_Start = models.CharField(max_length=21, null=True)
    OpenHomes_4_End = models.CharField(max_length=21, null=True)
    OpenHomes_4_Start = models.CharField(max_length=21, null=True)
    OpenHomes_5_End = models.CharField(max_length=21, null=True)
    OpenHomes_5_Start = models.CharField(max_length=21, null=True)
    OpenHomes_6_End = models.CharField(max_length=21, null=True)
    OpenHomes_6_Start = models.CharField(max_length=21, null=True)
    OpenHomes_7_End = models.CharField(max_length=21, null=True)
    OpenHomes_7_Start = models.CharField(max_length=21, null=True)
    RateableValue = models.FloatField(null=True)
    ViewingInstructions = models.CharField(max_length=255, null=True)
    job_run_datetime = models.DateTimeField(null=True)
