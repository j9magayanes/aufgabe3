def extract_names(json_data):
    names = []
    for item in json_data:
        if item["Name"] == "Body":
            for variable in item["Variables"]:
                names.append(variable["Name"])
    return names

json_data = [
    {
      "Name": "Header",
      "Variables": [
        {
          "Name": "eventHeader.eventId",
          "Type": "UInt32",
          "Value": "12461868"
        },
        {
          "Name": "eventHeader.eventName",
          "Type": "String",
          "Value": "partProcessed"
        },
        {
          "Name": "eventHeader.eventSwitch",
          "Type": "Int32",
          "Value": "132"
        },
        {
          "Name": "eventHeader.location.application",
          "Type": "String",
          "Value": "PLC"
        },
        {
          "Name": "eventHeader.location.fuNo",
          "Type": "String",
          "Value": "1"
        },
        {
          "Name": "eventHeader.location.lineNo",
          "Type": "String",
          "Value": "1201"
        },
        {
          "Name": "eventHeader.location.locationId",
          "Type": "String",
          "Value": "00000000120101400001100310000"
        },
        {
          "Name": "eventHeader.location.processName",
          "Type": "String",
          "Value": "Messen Ankerfreiweg"
        },
        {
          "Name": "eventHeader.location.processNo",
          "Type": "Int32",
          "Value": "121401031"
        },
        {
          "Name": "eventHeader.location.statIdx",
          "Type": "String",
          "Value": "1"
        },
        {
          "Name": "eventHeader.location.statNo",
          "Type": "String",
          "Value": "140"
        },
        {
          "Name": "eventHeader.location.toolPos",
          "Type": "String",
          "Value": "0"
        },
        {
          "Name": "eventHeader.location.workPos",
          "Type": "String",
          "Value": "31"
        },
        {
          "Name": "eventHeader.timeStamp",
          "Type": "DateTime",
          "Value": "09.04.2024 09:17:18"
        }
      ]
    },
    {
      "Name": "Event",
      "Variables": [
        {
          "Name": "partProcessed.identifier",
          "Type": "String",
          "Value": "0600_1201_0140_1234"
        }
      ]
    },
    {
      "Name": "Body",
      "Variables": [
        {
          "Name": "_A131_MeasurementDataOutProcess",
          "Type": "Array",
          "ArrayItems": [
            {
              "Name": "PartId",
              "Type": "String"
            },
            {
              "Name": "UniqueId",
              "Type": "String"
            },
            {
              "Name": "OrderNoCur",
              "Type": "String"
            },
            {
              "Name": "LocationId",
              "Type": "String"
            },
            {
              "Name": "0",
              "Type": "Array",
              "ArrayItems": [
                {
                  "Name": "PartId",
                  "Type": "String",
                  "Value": "0600_1201_0140_1234"
                },
                {
                  "Name": "UniqueId",
                  "Type": "String",
                  "Value": "0600_1201_0140_1234_240409_0001"
                },
                {
                  "Name": "OrderNoCur",
                  "Type": "String",
                  "Value": "82294"
                },
                {
                  "Name": "LocationId",
                  "Type": "String",
                  "Value": ""
                }
              ]
            }
          ]
        },
        {
          "Name": "_OpconResultStabiData",
          "Type": "Array",
          "ArrayItems": [
            {
              "Name": "Name",
              "Type": "String"
            },
            {
              "Name": "Value",
              "Type": "Single"
            },
            {
              "Name": "Unit",
              "Type": "String"
            },
            {
              "Name": "SetValue",
              "Type": "Single"
            },
            {
              "Name": "ValueLoLim",
              "Type": "Single"
            },
            {
              "Name": "ValueUpLim",
              "Type": "Single"
            },
            {
              "Name": "SwLoLim",
              "Type": "Single"
            },
            {
              "Name": "SwUpLim",
              "Type": "Single"
            },
            {
              "Name": "XqLoLim",
              "Type": "Single"
            },
            {
              "Name": "XqUpLim",
              "Type": "Single"
            },
            {
              "Name": "0",
              "Type": "Array",
              "ArrayItems": [
                {
                  "Name": "Name",
                  "Type": "String",
                  "Value": "ArmatureLift"
                },
                {
                  "Name": "Value",
                  "Type": "Single",
                  "Value": "-0,1195297"
                },
                {
                  "Name": "Unit",
                  "Type": "String",
                  "Value": "µm"
                },
                {
                  "Name": "SetValue",
                  "Type": "Single",
                  "Value": "78,2"
                },
                {
                  "Name": "ValueLoLim",
                  "Type": "Single",
                  "Value": "-10"
                },
                {
                  "Name": "ValueUpLim",
                  "Type": "Single",
                  "Value": "10"
                },
                {
                  "Name": "SwLoLim",
                  "Type": "Single",
                  "Value": "0,007"
                },
                {
                  "Name": "SwUpLim",
                  "Type": "Single",
                  "Value": "0,5"
                },
                {
                  "Name": "XqLoLim",
                  "Type": "Single",
                  "Value": "-0,86"
                },
                {
                  "Name": "XqUpLim",
                  "Type": "Single",
                  "Value": "0,86"
                }
              ]
            }
          ]
        },
        {
          "Name": "item.Process.LocationId",
          "Type": "String",
          "Value": ""
        },
        {
          "Name": "item.Process.OrderNoCur",
          "Type": "String",
          "Value": "82294"
        },
        {
          "Name": "item.Process.PartId",
          "Type": "String",
          "Value": "0600_1201_0140_1234"
        },
        {
          "Name": "item.Process.UniqueId",
          "Type": "String",
          "Value": "0600_1201_0140_1234_240409_0001"
        },
        {
          "Name": "item.Result.ArmatureLift.Name",
          "Type": "String",
          "Value": "ArmatureLift"
        },
        {
          "Name": "item.Result.ArmatureLift.SetValue",
          "Type": "Single",
          "Value": "78,2"
        },
        {
          "Name": "item.Result.ArmatureLift.SwLoLim",
          "Type": "Single",
          "Value": "0,007"
        },
        {
          "Name": "item.Result.ArmatureLift.SwUpLim",
          "Type": "Single",
          "Value": "0,5"
        },
        {
          "Name": "item.Result.ArmatureLift.Unit",
          "Type": "String",
          "Value": "µm"
        },
        {
          "Name": "item.Result.ArmatureLift.Value",
          "Type": "Single",
          "Value": "-0,1195297"
        },
        {
          "Name": "item.Result.ArmatureLift.ValueLoLim",
          "Type": "Single",
          "Value": "-10"
        },
        {
          "Name": "item.Result.ArmatureLift.ValueUpLim",
          "Type": "Single",
          "Value": "10"
        },
        {
          "Name": "item.Result.ArmatureLift.XqLoLim",
          "Type": "Single",
          "Value": "-0,86"
        },
        {
          "Name": "item.Result.ArmatureLift.XqUpLim",
          "Type": "Single",
          "Value": "0,86"
        },
        {
          "Name": "item.Result.MeasureIndex",
          "Type": "Int32",
          "Value": "1"
        },
        {
          "Name": "item.Result.MeasureIndexMax",
          "Type": "Int32",
          "Value": "3"
        },
        {
          "Name": "item.Result.OptionalParameter",
          "Type": "String",
          "Value": ""
        },
        {
          "Name": "item.Result.RTNest",
          "Type": "Int32",
          "Value": "0"
        },
        {
          "Name": "item.Result.SpecPartNo",
          "Type": "String",
          "Value": "LY_5201W010-002#2"
        },
        {
          "Name": "resHead.batch",
          "Type": "String",
          "Value": ""
        },
        {
          "Name": "resHead.machineID",
          "Type": "String",
          "Value": "967ed2ff-255c-4e91-a714-3a9d5a37707d"
        },
        {
          "Name": "resHead.nioBits",
          "Type": "Int32",
          "Value": "0"
        },
        {
          "Name": "resHead.result",
          "Type": "Int16",
          "Value": "9"
        },
        {
          "Name": "resHead.typeNo",
          "Type": "String",
          "Value": "F00VH12635"
        },
        {
          "Name": "resHead.typeVar",
          "Type": "String",
          "Value": ""
        },
        {
          "Name": "resHead.typeVersion",
          "Type": "String",
          "Value": ""
        },
        {
          "Name": "resHead.workingCode",
          "Type": "Int16",
          "Value": "6"
        },
        {
          "Name": "toolData",
          "Type": "Array"
        }
      ]
    },
    {
      "Name": "ResponseBody",
      "Variables": []
    },
    {
      "Name": "SymbolStore",
      "Variables": []
    }
  ]
names = extract_names(json_data)
print(names)
