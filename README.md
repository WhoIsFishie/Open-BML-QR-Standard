# Open-BML-QR-Standard

## Requirments
- Must fit withing a QR Code
- The data must be easily serializable and desirliazable on any programing language 
- the data must be readable even when scanned normaly (*this means the data must not be compressed to bypass requirment 1*)
- Must not use any propirotery technology for any of the steps as this is a Open Standard (*this rules out Microsoft Tags*)
- Data must be readable offline (*the data cant point to a website which then loads the details*)

### Current Suggestions
- [Heavy Json](http://https://github.com/WhoIsFishie/Open-BML-QR-Standard/blob/main/README.md#heavy-json "Heavy Json")
- [Json Lite](http://https://github.com/WhoIsFishie/Open-BML-QR-Standard/blob/main/README.md#lite-json "Json Lite")
- [INI](http://https://github.com/WhoIsFishie/Open-BML-QR-Standard/blob/main/README.md#ini "INI")



#### Heavy Json
[![](https://github.com/WhoIsFishie/Open-BML-QR-Standard/blob/main/Img/Heavy%20Json.png)](http://https://github.com/WhoIsFishie/Open-BML-QR-Standard/blob/main/Img/Heavy%20Json.png)
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
[![](https://github.com/WhoIsFishie/Open-BML-QR-Standard/blob/main/Img/Json%20Lite.png)](http://https://github.com/WhoIsFishie/Open-BML-QR-Standard/blob/main/Img/Json%20Lite.png)
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
[![](https://github.com/WhoIsFishie/Open-BML-QR-Standard/blob/main/Img/Ini.png)](http://https://github.com/WhoIsFishie/Open-BML-QR-Standard/blob/main/Img/Ini.png)
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
