const url = "http://127.0.0.1:8000";

function getRegions(): Promise<Array<string>> {
  return fetch(`${url}/api/get/regions`)
    .then((res) => res.json())
    .then((res) => res.data);
}

function getDepartments(): Promise<Array<string>> {
  return fetch(`${url}/api/get/departments`)
    .then((res) => res.json())
    .then((res) => res.data);
}

async function downloadReport(
  regionId: number,
  regionName: string,
  regionType: string
): Promise<void> {
  const myHeaders = new Headers();
  myHeaders.append("Content-Type", "application/json");

  const raw = JSON.stringify({
    region: regionId,
  });

  // eslint-disable-next-line @typescript-eslint/ban-types
  const requestOptions: Object = {
    method: "POST",
    headers: myHeaders,
    body: raw,
    redirect: "follow",
  };

  await fetch(`${url}/api/scrap-${regionType}`, requestOptions)
    .then(function (response) {
      return response.blob();
    })
    .then(function (blob) {
      const fileUrl = URL.createObjectURL(blob);
      const anchor = document.createElement("a");
      anchor.href = fileUrl;
      anchor.download = `${regionName}.docx`;
      document.body.appendChild(anchor);
      anchor.click();
      document.body.removeChild(anchor);
      URL.revokeObjectURL(fileUrl);
    });
}

export default {
  getRegions,
  getDepartments,
  downloadReport,
};
