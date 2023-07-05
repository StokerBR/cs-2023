import java.text.DateFormat;
import java.text.DecimalFormat;
import java.text.NumberFormat;
import java.util.Currency;
import java.util.Date;
import java.util.Locale;
import java.util.ResourceBundle;

public class InfoPaises {
    public static void main(String[] args) {
        String[] paises = {"US", "GB", "FR", "DE", "JP", "BR", "CN", "RU", "AU", "IN"};
        Locale[] locais = new Locale[paises.length];
        for (int i = 0; i < paises.length; i++) {
            locais[i] = new Locale(paises[i], paises[i]);
        }
        ResourceBundle bundle = ResourceBundle.getBundle("InfoPaisesBundle", Locale.getDefault());
        DateFormat formatoDataCurto = DateFormat.getDateInstance(DateFormat.SHORT, Locale.getDefault());
        DateFormat formatoDataLongo = DateFormat.getDateInstance(DateFormat.LONG, Locale.getDefault());
        DateFormat formatoHora = DateFormat.getTimeInstance(DateFormat.DEFAULT, Locale.getDefault());
        for (int i = 0; i < paises.length; i++) {
            System.out.println("País: " + locais[i].getDisplayCountry());
            System.out.println("Linguagem: " + locais[i].getDisplayLanguage());
            System.out.println("Formato de Data Curto: " + formatoDataCurto.format(new Date()));
            System.out.println("Formato de Data Longo: " + formatoDataLongo.format(new Date()));
            System.out.println("Formato de Hora: " + formatoHora.format(new Date()));
            Currency moeda = Currency.getInstance(locais[i]);
            NumberFormat formatoNumero = NumberFormat.getNumberInstance(locais[i]);
            System.out.println("Símbolo da Moeda Local: " + moeda.getSymbol());
            System.out.println("Separador Decimal: " + ((DecimalFormat) formatoNumero).getDecimalFormatSymbols().getDecimalSeparator());
            System.out.println("Separador de Milhar: " + ((DecimalFormat) formatoNumero).getDecimalFormatSymbols().getGroupingSeparator());
            System.out.println("Código de Página Windows: " + bundle.getString(paises[i] + ".codepage"));
            System.out.println();
        }
    }
}