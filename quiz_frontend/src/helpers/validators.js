import {
    regEx
} from './index';

const emailValidator = (rule, value = '', callback) => {
    if (value.length > 0) {
        const regex = regEx.EMAIL_REGEX;
        if (!regex.test(value)) {
            callback('Email should be valid.');
        }
    }
    callback();
    return;
};

const urlValidator = (rule, value = '', callback) => {
    if (value.length > 0) {
        const regex = regEx.URL_REGEX;
        if (!regex.test(value)) {
            callback('Link should be valid.');
        }
    }
    callback();
    return;
};

export default {
    emailValidator,
    urlValidator
};
