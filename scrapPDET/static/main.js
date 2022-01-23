async function scrapRegion(){
    const div = document.getElementById('loading');
    
    const url = 'http://127.0.0.1:8000/api/scrap-pdet';
    const region = document.getElementById('RegionPDET');
    const regionValue = region.value;
    const regionName = region.options[region.selectedIndex].text;
    
    div.innerHTML = '<strong>Loading...</strong><div class="progress"><div class="progress-bar progress-bar-striped progress-bar-animated bg-info" role="progressbar" aria-valuenow="100" aria-valuemin="0" aria-valuemax="100" style="width: 100%"></div></div>';
    const myHeaders = new Headers();
    myHeaders.append("Content-Type", "application/json");

    const raw = JSON.stringify({
    "region": regionValue
    });

    const requestOptions = {
    method: 'POST',
    headers: myHeaders,
    body: raw,
    redirect: 'follow'
    };

    const response = await fetch(url, requestOptions);
    const file = await response.blob();
    const fileURL = URL.createObjectURL(file);

    const anchor = document.createElement('a');
    anchor.href = fileURL;
    anchor.download = regionName+'.docx';
    document.body.appendChild(anchor);
    anchor.click();
    document.body.removeChild(anchor);
    URL.revokeObjectURL(fileURL);
    div.innerHTML = '';
};

async function scrapDeparment(){
    const div = document.getElementById('loading');

    const url = 'http://127.0.0.1:8000/api/scrap-department';
    const department = document.getElementById('Departamento');
    const departmentValue = department.value;
    const departmentName = department.options[department.selectedIndex].text;

    div.innerHTML = '<strong>Loading...</strong><div class="progress"><div class="progress-bar progress-bar-striped progress-bar-animated bg-info" role="progressbar" aria-valuenow="100" aria-valuemin="0" aria-valuemax="100" style="width: 100%"></div></div>';
    const myHeaders = new Headers();

    myHeaders.append("Content-Type", "application/json");

    const raw = JSON.stringify({
    "region": departmentValue
    });

    const requestOptions = {
    method: 'POST',
    headers: myHeaders,
    body: raw,
    redirect: 'follow'
    };

    const response = await fetch(url, requestOptions);
    const file = await response.blob();
    const fileURL = URL.createObjectURL(file);

    const anchor = document.createElement('a');
    anchor.href = fileURL;
    anchor.download = departmentName+'.docx';
    document.body.appendChild(anchor);
    anchor.click();
    document.body.removeChild(anchor);
    URL.revokeObjectURL(fileURL);
    div.innerHTML = '';
};