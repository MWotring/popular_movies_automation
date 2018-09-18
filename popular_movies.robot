*** Settings ***
Documentation    PopularMovies example tests

Library    Process
Library    AppiumLibrary
Library    PopularMovies.py

Test Setup      Run Keyword     Start PopularMoviesApp

*** Variables ***
${PACKAGE}      com.example.android.popularmovies
${ACTIVITY}     .MainActivity
${PLATFORM}     Android
${APPIUM_DRIVER_HOST}       http://0.0.0.0:4723/wd/hub

*** Test Cases ***
Verify Click On Movie And Open Details
    [Tags]    sanity
    verify_click_on_grid_element_and_open_detail_view

*** Keywords ***

Start PopularMoviesApp
    ${SERIAL_NO}    Run Process    adb    get-serialno
   AppiumLibrary.Open Application    ${APPIUM_DRIVER_HOST}  platformName=${PLATFORM}  deviceName=${SERIAL_NO.stdout}  appPackage=${PACKAGE}  appActivity=${ACTIVITY}
