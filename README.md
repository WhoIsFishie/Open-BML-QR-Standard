# Open-BML-QR-Standard

## Goal
to have all shops use the same QR code Scheme and have an opensource android and ios application to scan the QR for ease of use. this would also make shareing QR code of personal accounts easier if all devs come together and pick a standard to make apps for.

## Requirments
- Must fit withing a QR Code
- The data must be easily serializable and desirliazable on any programing language 
- the data must be readable even when scanned normaly (*this means the data must not be compressed to bypass requirment 1*)
- Must not use any propirotery technology for any of the steps as this is a Open Standard (*this rules out Microsoft Tags*)
- Data must be readable offline (*the data cant point to a website which then loads the details*)

### Current Suggestions
- [Heavy Json](https://github.com/WhoIsFishie/Open-BML-QR-Standard/blob/main/README.md#heavy-json "Heavy Json")
- [Json Lite](https://github.com/WhoIsFishie/Open-BML-QR-Standard/blob/main/README.md#lite-json "Json Lite")
- [INI](https://github.com/WhoIsFishie/Open-BML-QR-Standard/blob/main/README.md#ini "INI")
- [RAW 1](https://github.com/WhoIsFishie/Open-BML-QR-Standard/blob/main/README.md#raw-1 "RAW 1")
- [CSV](https://github.com/WhoIsFishie/Open-BML-QR-Standard/blob/main/README.md#csv "CSV")



#### Heavy Json
[![](https://github.com/WhoIsFishie/Open-BML-QR-Standard/blob/main/Img/Heavy%20Json.png)](https://github.com/WhoIsFishie/Open-BML-QR-Standard/blob/main/Img/Heavy%20Json.png)
```jsonc
{
    "BML_Data": [
        { 
            "AccountName": "Company Name - MVR",
            "AccountNumber": "7770-0000-12345",
            "AccountType": 0 //MVR
        },
        { 
            "AccountName": "Company Name - USD",
            "AccountNumber": "7770-0000-54321",
            "AccountType": 1 //USD
        }
    ],
    "Contacts": [
        { 
            "Token": "Telegram",
            "Value": "@Username"
        },
        { 
            "Token": "Viber",
            "Value": "+960 712 3456"
        }
    ],
    "Extra": [
        { 
            "Token": "Memo",
            "Value": "Please Include Your Invoice Number In the Remarks"
        }
    ],
    "Version": 1
}
```
this options allows to multiple types of data to be added in a very flexible way. it also supports multi account and multi contacts.

------------
#### Lite Json
[![](https://github.com/WhoIsFishie/Open-BML-QR-Standard/blob/main/Img/Json%20Lite.png)](https://github.com/WhoIsFishie/Open-BML-QR-Standard/blob/main/Img/Json%20Lite.png)
```jsonc
{
    "Ver": "2.0",
    //BML Account Number
    "AccNum": "7770-0000-54321",
    // Account Name as displayed on BML
    "Name": "Company Name - MVR",
    /// 1 = MVR
    /// 0 = USD
    "Type": 0,
    // contact number to send the payment slip to
    "Numb": "+960 712 3456"
}
```
this is a simpler and lighter version of Heavy Json but it only supports single contact and account

------------
#### INI
[![](https://github.com/WhoIsFishie/Open-BML-QR-Standard/blob/main/Img/Ini.png)](https://github.com/WhoIsFishie/Open-BML-QR-Standard/blob/main/Img/Ini.png)
```asp
Ver=3
//BML Account Number
AccNum=7770-0000-54321
// Account Name as displayed on BML
Name=Company Name - MVR
/// 1 = MVR
/// 0 = USD
Type=0
//contact number to send the payment slip to
Numb=+960 712 3456
```
an alternetive to json as there are less characters being used.

------------
#### RAW 1
[![](https://github.com/WhoIsFishie/Open-BML-QR-Standard/blob/main/Img/RAW1.png)](https://github.com/WhoIsFishie/Open-BML-QR-Standard/blob/main/Img/RAW1.png)
```txt
//BML Account Number
7770-0000-54321
Company Name
1
+960 712 3456
```
this is a raw text version where regex is used to detect contact number and account number. a single digit is assigned to the Currency and the account name will be the only string

------------
#### CSV
[![](https://github.com/WhoIsFishie/Open-BML-QR-Standard/blob/main/Img/CSV.png)](https://github.com/WhoIsFishie/Open-BML-QR-Standard/blob/main/Img/CSV.png)
```txt
7770-0000-54321,7770-0000-12345
Company Name,Company Name
1,0
Viber,Telegram
+960 712 3456,@username
```
an updated version of RAW 1
this method uses CSV and Regex as well as line numbers to phase the text. this method is very readable but not easily scalable. in place of CSV we could also use TSV

------------
#### NText
![image](https://user-images.githubusercontent.com/83373559/199571658-26e7ccbe-9f91-4d7c-a4e3-02e18e2dfc5c.png)
```NextedText
BANK:
    A:
        >Company Name
        >7777000001234
        >0
    B:
        >Company Name
        >7777000001234
        >1
viber:7123456
```
[Nested Text](https://nestedtext.org/en/stable/) is a simpler and much more readable alternative to JSON 
