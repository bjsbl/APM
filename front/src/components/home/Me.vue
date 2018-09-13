<template>
  <section>
    <el-collapse v-model="activeNames">
      <el-collapse-item title="项目A" name="1">
        <el-row :gutter="10">
          <el-col :span="12">
          <el-card class="box-card">
            <div slot="header" class="clearfix">
              <span>项目统计</span>
              <el-button style="float: right; padding: 3px 0" type="text">操作按钮</el-button>
            </div>
            <el-row>
              <el-col>
                <div id="testResultChart" :style="{width:'100%', height: '300px'}"></div>
              </el-col>
            </el-row>
          </el-card>
        </el-col>
          <el-col :span="12">
            <el-card class="box-card">
            <div slot="header" class="clearfix">
              <span>错误率统计</span>
              <el-button style="float: right; padding: 3px 0" type="text">操作按钮</el-button>
            </div>
            <el-row>
              <el-col>
                <div id="apiChart" :style="{width:'100%', height: '300px'}"></div>
              </el-col>
            </el-row>
          </el-card>
          </el-col>
        </el-row>
      </el-collapse-item>
    </el-collapse>
  </section>
</template>

<script>
  export default{
    data(){
      return{
        activeNames:['1']
      }
    },
    methods:{
      showApiCharts(){
        let myChart = this.$echarts.init(document.getElementById('testResultChart'))
        let apiChart = this.$echarts.init(document.getElementById('apiChart'))
        let option = {
          tooltip: {
              trigger: 'item',
              formatter: "{a} <br/>{b}: {c} ({d}%)"
          },
          legend: {
              orient: 'vertical',
              x: 'left',
              data:['待测试','已通过','未通过']
          },
          series: [
              {
                  name:'访问来源',
                  type:'pie',
                  radius: ['50%', '70%'],
                  avoidLabelOverlap: false,
                  label: {
                      normal: {
                          show: false,
                          position: 'center'
                      },
                      emphasis: {
                          show: true,
                          textStyle: {
                              fontSize: '30',
                              fontWeight: 'bold'
                          }
                      }
                  },
                  labelLine: {
                      normal: {
                          show: false
                      }
                  },
                  data:[
                      {value:335, name:'待测试'},
                      {value:310, name:'已通过'},
                      {value:234, name:'未通过'}
                  ]
              }
          ]
        };
        myChart.setOption(option);
        option = {
            grid: {
                left: '3%',
                right: '4%',
                bottom: '3%',
                containLabel: true
            },
            tooltip: {
                trigger: 'axis'
            },
            xAxis: {
                type: 'category',
                data: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
            },
            yAxis: {
                type: 'value'
            },
            series: [{
                data: [820, 932, 901, 934, 1290, 1330, 1320],
                type: 'line'
            }]
        };

        apiChart.setOption(option);
      }
    },
    mounted(){
      this.showApiCharts()
    }
  }
</script>