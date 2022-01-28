import { SwalNotification } from "./utils/SwalNotification.js";
import { request } from "./utils/request.js";
import { validarSoloNumeros, validarCampos } from "./utils/validaciones.js";

const title = document.title;

const API_URL = window.origin;

const registrar_participante = async () => {
    const data = await request(`${API_URL}/registrar_participante/`, "POST", {
        codigo: String(txtCodigo.value).trim().toUpperCase(),
        nombreCompleto: String(txtNombreCompleto.value).trim(),
        correo: String(txtCorreo.value).trim(),
        celular: String(txtCelular.value).trim()
    });
    if (data.mensaje === "EXITO") {
        limpiarCampos();
        SwalNotification(title, "¡Se ha registrado su participación exitosamente!", "success", "Ok");
    } else if (data.mensaje === "CODIGONOVALIDO") {
        SwalNotification(title, "Código no válido: no existe o ya fue registrado.", "info", "Ok");
    } else {
        SwalNotification(title, "Ocurrió un error inesperado...", "error", "Ok");
    }
};

const limpiarCampos = () => {
    frmRegistroParticipante.reset();
    txtCodigo.focus();
};

window.addEventListener("DOMContentLoaded", () => {
    txtCelular.addEventListener("keypress", function (e) {
        if (!validarSoloNumeros(e)) {
            e.preventDefault();
        }
    });

    frmRegistroParticipante.addEventListener("submit", (e) => {
        e.preventDefault();
        if (validarCampos()) {
            registrar_participante();
        }
    });
});
