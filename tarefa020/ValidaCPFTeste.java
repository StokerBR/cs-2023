package br.com.gilmarioarantes.validacpf.model;

import static org.testng.Assert.*;
import org.testng.annotations.Test;

public class ValidaCPFTeste {

    @Test
    public void testaCPFValido() {
        ValidaCPF validaCPF = new ValidaCPF();
        boolean resultado = validaCPF.isCPF("12345678909");
        assertTrue(resultado);
    }

    @Test
    public void testaCPFFormatoInvalido() {
        ValidaCPF validaCPF = new ValidaCPF();
        boolean resultado = validaCPF.isCPF("123.456.789-09");
        assertFalse(resultado);
    }

    @Test
    public void testaCPFQuantidadeDigitosInvalida() {
        ValidaCPF validaCPF = new ValidaCPF();
        boolean resultado = validaCPF.isCPF("1234567890");
        assertFalse(resultado);
    }

    @Test
    public void testaCPFComCaracteresInvalidos() {
        ValidaCPF validaCPF = new ValidaCPF();
        boolean resultado = validaCPF.isCPF("1234567890a");
        assertFalse(resultado);
    }

    @Test
    public void testaCPFComDigitosRepetidos() {
        ValidaCPF validaCPF = new ValidaCPF();
        boolean resultado = validaCPF.isCPF("11111111111");
        assertFalse(resultado);
    }

    @Test
    public void testaCPFInvalido() {
        ValidaCPF validaCPF = new ValidaCPF();
        boolean resultado = validaCPF.isCPF("12345678901");
        assertFalse(resultado);
    }
}