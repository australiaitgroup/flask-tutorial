const openMobileMenu = () => {
    const mobileMenuWrapper = document.querySelector(".header__mobile-menu-wrapper");
    mobileMenuWrapper.classList.remove("closed");
    mobileMenuWrapper.classList.add("opened");
}

const closeMobileMenu = () => {
    const mobileMenuWrapper = document.querySelector(".header__mobile-menu-wrapper");
    mobileMenuWrapper.classList.remove("opened");
    mobileMenuWrapper.classList.add("closed");
}

const toggleSearchField = () => {
    const mobileSearchBar = document.querySelector(".header__mobile-search-area");
    if(!mobileSearchBar.classList.contains("opened")) {
        mobileSearchBar.classList.add("opened")
        mobileSearchBar.classList.remove("closed")
    } else {
        mobileSearchBar.classList.add("closed")
        mobileSearchBar.classList.remove("opened")
    }
}