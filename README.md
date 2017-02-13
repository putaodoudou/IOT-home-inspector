#Internet of Things Home Inspector

**Purpose:** To identify and provide resources for updates to your Internet of Things devices whether you search for them on the site or connect your IoT device directly to our site.

**Authors**

Rick Valenzuela

Regenal Grant

Joseph Derosa

Conor Clary

**Setup Instructions**
```
git clone https://github.com/rveeblefetzer/IOT-home-inspector.git
```

## Two-factor authentication
Any visitor can use the site's basic function of entering a device model and receiving information on the current software and/or firmware versions. Registered users can use the site to maintain a list of their devices. All registered users must log in with two-factor authentication, which is implemented through the django-two-factor-auth library. Currently this is implemented through time-based tokens using an app such as Google Authenticator or Authy. Site admins must also use two-factor authentication.
