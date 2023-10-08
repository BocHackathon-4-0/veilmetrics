function parseCSVLine(line) {
    const results = [];
    let startValueIndex = 0;
    let insideQuote = false;

    for (let i = 0; i < line.length; i++) {
        if (line[i] === '"') {
            insideQuote = !insideQuote;
        } else if (line[i] === ',' && !insideQuote) {
            results.push(line.substring(startValueIndex, i));
            startValueIndex = i + 1;
        }
    }
    results.push(line.substring(startValueIndex));

    // Remove quotes from the parsed values
    return results.map(value => value.startsWith('"') && value.endsWith('"') ? value.slice(1, -1) : value);
}

function downloadJSON(data, filename) {
    console.log(data);
    const dataStr = "data:text/json;charset=utf-8," + encodeURIComponent(JSON.stringify(data, null, 4));
    const downloadAnchorNode = document.createElement('a');
    downloadAnchorNode.setAttribute("href", dataStr);
    downloadAnchorNode.setAttribute("download", filename);
    document.body.appendChild(downloadAnchorNode); // Required for Firefox
    downloadAnchorNode.click();
    downloadAnchorNode.remove();
}

let width, height, gradient;
function getGradient(ctx, chartArea) {
    const chartWidth = chartArea.right - chartArea.left;
    const chartHeight = chartArea.bottom - chartArea.top;
    if (gradient === null || width !== chartWidth || height !== chartHeight) {
        // Create the gradient because this is either the first render
        // or the size of the chart has changed
        width = chartWidth;
        height = chartHeight;
        gradient = ctx.createLinearGradient(0, chartArea.bottom, 0, chartArea.top);
        gradient.addColorStop(0, 'rgb(255, 0, 0)');
        gradient.addColorStop(0.25, 'rgb(255, 167, 0)');
        gradient.addColorStop(0.5, 'rgb(255, 244, 0)');
        gradient.addColorStop(0.75, 'rgb(163, 255, 0)');
        gradient.addColorStop(1, 'rgb(44, 186, 0)');
    }

    return gradient;
}


const ctx3 = document.getElementById('btc-add').getContext('2d');

fetch("btc_on-chain.json")
    .then(response => response.json())
    .then(json => createCharts(json));

function createCharts(input_data){
    btcOnChainData = input_data;
    const data = {
        labels: input_data.date,
        datasets: [
            {
                label: '$1',
                data: input_data.AdrBalUSD1Cnt,
                fill: false,
                borderColor: 'rgb(75, 192, 192)',
                tension: 0.1
            },
            {
                label: '$10',
                data: input_data.AdrBalUSD10Cnt,
                fill: false,
                borderColor: 'rgb(50, 254, 0)',
                tension: 0.1
            },
            {
                label: '$100',
                data: input_data.AdrBalUSD100Cnt,
                fill: false,
                borderColor: 'rgb(50, 2, 0)',
                tension: 0.1
            },
            {
                label: '$1K',
                data: input_data.AdrBalUSD1KCnt,
                fill: false,
                borderColor: 'rgb(124, 25, 0)',
                tension: 0.1
            },
            {
                label: '$10k',
                data: input_data.AdrBalUSD10KCnt,
                fill: false,
                borderColor: 'rgb(164, 24, 192)',
                tension: 0.1
            },
            {
                label: '$100K',
                data: input_data.AdrBalUSD100KCnt,
                fill: false,
                borderColor: 'rgb(50, 2, 192)',
                tension: 0.1
            },
            {
                label: '$1M',
                data: input_data.AdrBalUSD1MCnt,
                fill: false,
                borderColor: 'rgb(40, 250, 250)',
                tension: 0.1
            },
            {
                label: '$10M',
                data: input_data.AdrBalUSD10MCnt,
                fill: false,
                borderColor: 'rgb(120, 210, 120)',
                tension: 0.1
            }
        ]
    };

    const myChart23= new Chart(ctx3, {
        type: 'line',
        data: data,
        options: {
            responsive: true,
            elements: {
                point:{
                    radius: 0
                }
            }
        }
    });

}

// IMSI
fetch("imsi_data.json")
    .then(response => response.json())
    .then(json => createIMSI(json));

function createIMSI(json){


    for (var i = 0; i < json.dates.length; i++) {
        imsi_output_data.push({
            date: json.dates[i],
            score: json.index[i],
        });
    }

    // Sentiment Time series
    const ctx = document.getElementById('imsi').getContext('2d');

    const imsiData = {
        labels: json.dates,
        datasets: [
            {
                label: 'IMSI',
                data: json.index,
                borderColor: function(context) {
                    const chart = context.chart;
                    const {ctx, chartArea} = chart;

                    if (!chartArea) {
                        // This case happens on initial chart load
                        return null;
                    }
                    return getGradient(ctx, chartArea);
                },
                borderWidth: 5,
                cubicInterpolationMode: 'monotone',
            }
        ]
    };

    const imsiChart= new Chart(ctx, {
        type: 'line',
        data: imsiData,
        options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
                legend: {
                    display: false,
                }
            },
            elements: {
                point:{
                    radius: 0
                }
            },
            scales: {
                y: {
                    min: 20,
                    max: 50,
                }
            }
        }
    });
}

// MEDIA WEIGHTS CHART

const ctx2 = document.getElementById('media_weights').getContext('2d');
const polarData = {
    labels: ["Decrypt",
        "Forbes",
        "U.Today",
        "Cointelegraph",
        "BeInCrypto",
        'Bitcoin.com',
        'Bitcoinist',
        'Blockworks',
        'Bitcoin Magazine' ,
        'The Block',
        'Crypto Daily',
        'CoinGape',
        'The Daily Hodl',
        'AMBCrypto',
        'CryptoPotato'],

    datasets: [{
        label: 'Media Weighted Importance',
        data: [0.09652926987731078, 0.03663349267765613, 0.07407413239935122, 0.055460946109427034, 0.06187885864439882, 0.044842926479574524, 0.06437240523303199, 0.14266841615212875, 0.055019317835501014, 0.05467964940732963, 0.046599511531016796, 0.05771158252023148, 0.06508818270108721, 0.06186458228300769, 0.08257672614894694],
        //data: [0.05,0.05,0.05,0.05,0.05,0.05,0.05,0.05,0.05,0.05,0.05,0.05,0.05,0.05,0.05],
        backgroundColor: [
            'rgb(250, 191, 44,0.75)',
            'rgb(75, 192, 192,0.75)',
            'rgb(38, 205, 156,0.75)',
            'rgb(38, 50, 56,0.75)',
            'rgb(53, 53, 53,0.75)',
            'rgb(254, 211, 25,0.75)',
            'rgb(205, 45, 98,0.75)',
            'rgb(0, 0, 0,0.75)',
            'rgb(16, 116, 183,0.75)',
            'rgb(0, 167, 97,0.75)',
            'rgb(35, 31, 32,0.75)',
            'rgb(255, 149, 0,0.75)',
            'rgb(79, 46, 185,0.75)',
            'rgb(0, 153, 253,0.75)',
            'rgb(24, 23, 22,0.75)'
        ]
    }]
};

const myChart2 = new Chart(ctx2, {
    type: 'polarArea',
    data: polarData,
    options: {
        responsive: true,
        maintainAspectRatio: false,
        layout: {
            padding: 0
        },
        scales: {
            r: {
                pointLabels: {
                    display: true,
                    centerPointLabels: true,
                    font: {
                        size: 16
                    }
                }
            }
        },
        plugins: {
            legend: {
                position: 'bottom',
            }
        }
    }
});


// const dataFile = {"index": [45.7492305, 45.40989, 49.707133944, 40.443697404, 52.298805475, 40.001313, 49.442881316, 43.25746506, 50.420],
//     "index2": [15, 44.40989, 59.707133944, 30.443697404, 34.298805475, 51.001313, 12.442881316, 90.25746506, 150.420],
//     "index3": [0.7492305, 5.40989, 5.707133944, 23.443697404, 34.298805475, 56.001313, 34.442881316, 77.25746506, 88.420],
//                                     "dates": ["06 Apr, 2022", "07 Apr, 2022", "08 Apr, 2022", "09 Apr, 2022", "10 Apr, 2022", "11 Apr, 2022", "12 Apr, 2022", "13 Apr, 2022", "14 Apr, 2022"]}
// const data = {
//     labels: dataFile.dates,
//     datasets: [
//         {
//             label: 'My First Dataset',
//             data: dataFile.index,
//             fill: false,
//             borderColor: 'rgb(75, 192, 192)',
//             tension: 0.1
//         },
//         {
//             label: 'My second Dataset',
//             data: dataFile.index2,
//             fill: false,
//             borderColor: 'rgb(50, 2, 192)',
//             tension: 0.1
//         },
//         {
//             label: 'My third Dataset',
//             data: dataFile.index3,
//             fill: false,
//             borderColor: 'rgb(164, 24, 192)',
//             tension: 0.1
//         }
//     ]
// };

function populateBTCHistoricalTable(data) {
    const rows = data.split('\n');

    // Skip the header row by starting from index 1
    for (let i = 1; i < rows.length; i++) {
        const columns = parseCSVLine(rows[i])

        if (columns.length == 1){
            console.log("ETO REEEE")
        }else {

            const date = columns[1];
            const price = columns[2];
            const marketcap = columns[3];
            const volume = columns[4];

            btcHistoricalTable.row.add([date, price, marketcap, volume]).draw(false);
            btcHistoricalData.push({
                date: date,
                close_price: price,
                marketcap: marketcap,
                volume: volume
            });
        }
    }
}

$('#uploadForm').on('submit', function(e) {
    e.preventDefault();

    var formData = new FormData(this);
    console.log(formData);

    $.ajax({
        url: 'upload.php',
        type: 'POST',
        data: formData,
        success: function(data) {
            $('#message').text(data);
        },
        cache: false,
        contentType: false,
        processData: false
    });
});

let pdf_file;
$('#pdfFile').on('change', function() {
    pdf_file = $(this).val().split('\\').pop();
    //alert(pdf_file)
});

