import { SwalNotification } from "./SwalNotification.js";

const validarSoloNumeros = (e) => {
    let k = document.all ? e.keyCode : e.which;
    if (k === 8 || k === 0) return true;
    const patron = /\d/;
    let n = String.fromCharCode(k);
    return patron.test(n);
};

const validarCorreo = (correo) => {
    const regex = /[\w-\.]{2,}@([\w-]{2,}\.)*([\w-]{2,}\.)[\w-]{2,4}/;
    return regex.test(correo);
};

const validarCampos = () => {
    let mensajeAlerta = "";
    let codigo = String(txtCodigo.value).trim();
    if (codigo.length === 4) {
        let nombreCompleto = String(txtNombreCompleto.value).trim();
        if (nombreCompleto.length >= 15 && nombreCompleto.length <= 50) {
            let correo = String(txtCorreo.value).trim();
            if (correo.length >= 10 && correo.length <= 50) {
                if (validarCorreo(correo)) {
                    let celular = String(txtCelular.value).trim();
                    if (celular.length === 8) {
                        return true;
                    } else {
                        mensajeAlerta = "El celular debe tener 8 dígitos.";
                    }
                } else {
                    mensajeAlerta = "Debe ingresar un correo válido. Ejm: nombre@gmail.com";
                }
            } else {
                mensajeAlerta = "El correo debe tener entre 10 y 50 caracteres.";
            }
        } else {
            mensajeAlerta = "El nombre completo debe tener entre 25 y 50 caracteres.";
        }
    } else {
        mensajeAlerta = "El código debe tener 4 caracteres.";
    }
    SwalNotification(document.title, mensajeAlerta, "info", "Ok");
    return false;
};

export { validarSoloNumeros, validarCampos };
