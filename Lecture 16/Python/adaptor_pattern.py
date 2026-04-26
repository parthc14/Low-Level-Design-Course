from abc import ABC, abstractmethod

class IReport(ABC):
    @abstractmethod
    def get_JSON_data(self) -> str:
        pass


class XMLDataProvider:
    def get_XML_data(self, data: str):
        sep = data.index(":")
        name = data[0:sep]
        id = data[sep + 1:]

        return "<user>"+ "<name>" + name + "</name>" + "<id>"   + id   + "</id>"+ "</user>"


class XMLDataProviderAdaptor(IReport):
    def __init__(self, provider: XMLDataProvider):
        self.__provider = provider
    
    def provides_xml(self):
        return self.__provider

    def get_JSON_data(self, data: str):
        xml = self.provides_xml().get_XML_data(data)
        start_name = xml.index("<name>") + 6
        end_name = xml.index("</name>")

        name = xml[start_name: end_name]

        start_id = xml.index("<id>") + 4
        end_id = xml.index("</id>")

        id = xml[start_id: end_id]

        return "{\"name\":\"" + name + "\", \"id\":" + id + "}"


class Client:
    def get_report(self, report: IReport, raw_data: str):
        print(f"Processed JSON: {report.get_JSON_data(raw_data)}")


if __name__ == "__main__":
    xml_prov = XMLDataProvider()

    adaptor = XMLDataProviderAdaptor(xml_prov)

    raw_data = "Alice:42"

    client = Client()
    client.get_report(adaptor, raw_data)

