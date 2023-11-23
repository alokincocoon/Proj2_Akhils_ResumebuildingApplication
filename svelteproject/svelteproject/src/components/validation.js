// Function to validate the user's full name
export function validateFullName(fullname) {
    let error = "";
    if (fullname.trim() === "") {
        error = "Please enter your name";
    } else if (fullname.length < 3) {
        error = "Name length must be minimum 3 letters";
    }
    //An error message if the full name is invalid, or an empty string if it is valid
    return error;
}
// Function to validate the user's phone number
export function validatePhone(phone) {
    const regexmob = /^\d{10}$/;
    let error = "";

    if (phone.trim() == "") {
        error = "Please enter your phone number";
        return error;
    } else if (!regexmob.test(phone)) {
        error = "entered phone number is not valid";
        return error;
    }
    // An error message if the phone number is invalid, or an empty string if it is valid
    return error;
}
// Function to validate the user's email address
export function validateEmail(email) {
    const emailpattern =
        /^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$/;
    let error = "";

    if (email.trim() === "") {
        error = "Please enter your email";
        return error;
    } else if (!emailpattern.test(email)) {
        error = "entered email address is not valid";
        return error;
    }
    // console.log(error);
    //An error message if the email address is invalid, or an empty string if it is valid
    return error;
}
// Function to validate the user's image URL
export function validateImageUrl(imageurl) {
    const urlpattern =
        /(?:https?):\/\/(\w+:?\w*)?(\S+)(:\d+)?(\/|\/([\w#!:.?+=&%!\-\/]))?/;
    let error = "";
    if (imageurl.trim() == "") {
        error = "Please enter image URL";
        return error;
    } else if (!urlpattern.test(imageurl)) {
        error = "entered url is not valid";
        return error;
    }
    // console.log(error);
    //An error message if the image URL is invalid, or an empty string if it is valid
    return error;
}
// Function to validate the user's summary
export function validateSummary(summary) {
    let error = "";
    if (summary.trim() == "") {
        error = "summary cannot be empty";
    } else if (summary.length < 10) {
        error = "enter a valid summary";
    }
    //   An error message if the summary is invalid, or an empty string if it is valid
    return error;
}
// Function to validate the user's address
export function validateAddress(address_line) {
    let error = "";
    if (address_line.trim() === "") {
        error = "Please enter your address";
    }
    //   An error message if the address is invalid, or an empty string if it is valid
    return error;
}
// Function to validate the user's city
export function validateCity(city) {
    let error = "";
    if (city.trim() == "") {
        error = "Please enter your city";
    }
    //   An error message if the city is invalid, or an empty string if it is valid
    return error;
}
// Function to validate the user's state
export function validateState(state) {
    let error = "";
    if (state.trim() == "") {
        error = "Please enter your state";
    }
    //   An error message if the state is invalid, or an empty string if it is valid
    return error;
}
// Function to validate the user's country
export function validateCountry(country) {
    let error = "";
    if (country.value == "") {
        error = "Please select your country";
    }
    //   An error message if the country is invalid, or an empty string if it is valid
    return error;
}
// Function to validate the user's qualification
export function validateQualification(qualification) {
    let error = "";
    if (qualification.trim() == "") {
        error = "Please enter your qualification";
    }
    //   An error message if the qualification is invalid, or an empty string if it is valid
    return error;
}
// Function to validate the user's course name
export function validateCourseName(course_name) {
    let error = "";
    if (course_name.trim() == "") {
        error = "Please enter your course name";
    }
    //   An error message if the course name is invalid, or an empty string if it is valid
    return error;
}
// Function to validate the user's insttute
export function validateInstitute(institute_name) {
    let error = "";
    if (institute_name.trim() == "") {
        error = "Please enter your institute name";
    }
    //   An error message if the insttute is invalid, or an empty string if it is valid
    return error;
}
// Function to validate the user's location
export function validateInstituteLocation(location) {
    let error = "";
    if (location.trim() == "") {
        error = "Please enter your institute location";
    }
    //   An error message if the location is invalid, or an empty string if it is valid
    return error;
}
export function validateZipcode(zip_code) {
    let error = "";
    if (zip_code.trim() == "") {
        error = "Please enter your zipcode";
    }
    //   An error message if the zipcode is invalid, or an empty string if it is valid
    return error;
}

