$(document).ready(function() {  
            var chart = {
               type: 'pie',
               options3d: {
                  enabled: true,
                  alpha: 45         
               }
            };
            var title = {
               text: 'Contents of Highsoft\'s weekly fruit delivery'   
            };   
            var subtitle = {
               text: '3D donut in Highcharts'
            };  
            var plotOptions = {
               pie: {
                  innerSize: 100,
                  depth: 45
               }
            };   
            var series = [{
               name: 'Delivered amount',
               data: [
                  ['Bananas', 8],
                  ['Kiwi', 3],
                  ['Mixed nuts', 1],
                  ['Oranges', 6],
                  ['Apples', 8],
                  ['Pears', 4],
                  ['Clementines', 4],
                  ['Reddish (bag)', 1],
                  ['Grapes (bunch)', 1]
               ]
            }];     
            
            var json = {};   
            json.chart = chart; 
            json.title = title;       
            json.subtitle = subtitle; 
            json.plotOptions = plotOptions; 
            json.series = series;   
            $('#pie1').highcharts(json);
            $('#pie2').highcharts(json);
         });