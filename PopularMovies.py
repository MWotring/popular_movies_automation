from robot.libraries.BuiltIn import BuiltIn


class PopularMovies:

    def __init__(self):
        self.appium_library = BuiltIn().get_library_instance("Appium Library")

    GRID_MOVIE_BASE = "android = UiSelector()" \
                      ".resourceId(\"com.example.android.popularmovies:id/recyclerview_movies\")" \
                      ".childSelector(UiSelector().className(\"android.widget.FrameLayout\").index({})" \
                      ".childSelector(UiSelector().resourceId(\"com.example.android.popularmovies:id/movie_image\")))"

    MOVIE_TITLE_ID = "id=original_title_txt"
    MOVIE_RATING_ID = "id=movie_rated"
    MOVIE_RELEASE_ID = "id=movie_released"
    MOVIE_SYNOPSIS_ID = "id=movie_synopsis"
    MOVIE_TRAILER_BASE = "android = UiSelector()" \
                         ".resourceId(\"com.example.android.popularmovies:id/rv_movie_trailers\")" \
                         ".childSelector(UiSelector().className(\"android.widget.LinearLayout\").index({})" \
                         ".childSelector(UiSelector()" \
                         ".resourceId(\"com.example.android.popularmovies:id/trailer_item\")))"

    def verify_click_on_grid_element_and_open_detail_view(self):
        self.appium_library.wait_until_page_contains_element(self.GRID_MOVIE_BASE.format(0))
        self.appium_library.click_element(self.GRID_MOVIE_BASE.format(0))
        self.appium_library.wait_until_page_contains_element(self.MOVIE_TITLE_ID)