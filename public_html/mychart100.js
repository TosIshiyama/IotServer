//https://qiita.com/tabetomo/items/355f00180095eff37d23 参考

// https://gist.github.com/tigawa/8858345
// http://uxmilk.jp/11586

function csv2Array(str) {
  var csvData = [];
  str = str.replace(/\r\n/g, '\n'); // CRを削除
  str = str.replace(/\n+/g, '\n'); // 空行を削除
  str = str.replace(/\s+,|,\s+/g, ','); // 不要な空白を削除
  var lines = str.split('\n');
  var ii=0;
  if( lines.length > 100 ) ii = lines.length - 100;
  for (var i = ii; i < lines.length; i++) {
    var cells = lines[i].split(",");
    csvData.push(cells);
  }
  return csvData;
}

// リクエストにjqueryを利用する場合
function main_jquery() {
  var csvData = $.ajax({
    url: 'data.csv',
    dataType: 'text',
    cache: false
  }).then(function (resText) {
    var data = csv2Array(resText);

    // print raw data
    var target = document.getElementById("rawdata");
    target.innerText = resText;
    // plot chart
    drawBarChart(data)
  })

}

// リクエストにjqueryを利用しない場合
function main_nojquery() {
  var req = new XMLHttpRequest();
  var filePath = 'data.csv';
  req.open("GET", filePath, true); //true:非同期,false:同期
  req.onload = function () {
    var resText = req.responseText;
    data = csv2Array(resText);

    // print raw data
    var target = document.getElementById("rawdata");
    target.innerText = resText;
    // plot chart
    drawBarChart(data);
  }
  req.send(null);
}

// colormapもどき
function mycolmap(l) {
  // https://github.com/bpostlethwaite/colormap/blob/master/index.js
  function rgbaStr(rgba) {
    return 'rgba(' + rgba.join(',') + ')';
  }
  // http://stackoverflow.com/questions/20306650/color-list-items-from-a-range-of-colors
  var cStr = [];
  var color_from = [54, 162, 235, 0.3];
  var color_to = [255, 99, 132, 0.3];
  var l1 = l - 1;
  for (var i = 0; i < l; i++) {
    var c = [];
    var j = 0;
    for (; j < 3; ++j) {
      c[j] = Math.floor(color_from[j] * (l1 - i) / l1 + color_to[j] * (i) / l1);
    }
    // alpha doesn't need floor
    c[j] = color_from[j] * (l1 - i) / l1 + color_to[j] * (i) / l1;
    cStr[i] = rgbaStr(c)
  }
  return cStr;
}

// common part
// http://stackoverflow.com/questions/32977262/loading-an-external-json-into-chartjs
// http://microbuilder.io/blog/2016/01/10/plotting-json-data-with-chart-js.html
// https://www.webtoolnavi.com/chart-js/
function drawBarChart(data) {
  // set chart labels and data
  var tmpLabels = [];
  var dataList = [];
  var nameList = ["A Point", "B Point", "C Point"];
  var numData = data[0].length-1;  // とりあえず先頭行の列数からデータ数を導出する
//  var bgcolList = ["rgba(54,162,235,0.2)","rgba(255,99,132,0.2)"];
  var bgcolList = mycolmap(numData);

  for (var i = 0; i < numData; i++) {
    dataList[i] = [];
  }
  for (var row in data) {
    tmpLabels.push(data[row][0])
    for (var i = 0; i < numData; i++) {
      dataList[i].push(data[row][i+1]);
    }
  };

  var datasetList = [];
  for (var i = 0; i < numData; i++) {
    datasetList.push({
      label: nameList[i],
	  fill: false,
	  borderColor: bgcolList[i],
      data: dataList[i]
    });
  }

  var chartData = {
    labels: tmpLabels,
    datasets: datasetList
  };

  var ctx = document.getElementById("myChart").getContext("2d");
  ctx.canvas.width = 1000;
  ctx.canvas.height = 600;
  // for chart.js 2.0
  // <script src="http://cdnjs.cloudflare.com/ajax/libs/Chart.js/2.3.0/Chart.min.js"></script>
  var myChart = new Chart(ctx, {
    type: 'line',
    data: chartData,
	options: {
      scales: {
        xAxes: [{
          ticks: {
            autoSkip: false,
            maxRotation: 90,
            minRotation: 90
          }
        }],
        yAxes: [{
          scaleLabel: {
            display: true,
            labelString: 'temprature',
            fontSize: 14
          }
        }]
      },
      legend: {
        display: true,
        position: 'right'
      },
  	  animation: false
    }
  });
}

// ここがメイン
function main() {
  main_jquery();
  //main_nojquery();
  setTimeout("location.reload()",1000);
}

main();