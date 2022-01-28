import { SwalNotification } from "./SwalNotification.js";

const title = document.title;

const request = async (API_URL, method = "GET", body = {}) => {
    let options = {};

    if (method !== "GET") {
        options = {
            method: method,
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(body)
        };
    }

    try {
        const response = await fetch(API_URL, options);
        return await response.json();
    } catch (ex) {
        SwalNotification(title, "Ocurrió un error inesperado...", "error", "Ok");
    }
};

export { request };
