<template>
  <el-row>
    <el-col :span="24">
      <el-row>
      <el-col :span='24'>
        <el-button type='primary' @click='addTask'>新增用例</el-button>
      </el-col>
    </el-row>
      <el-table :data="taskList" highlight-current-row v-loading="listLoading">
        <el-table-column prop="name" label="名称" sortable>
          <template slot-scope="scope">
            <router-link :to="'/case/api'">{{scope.row.name }}</router-link>
          </template>
        </el-table-column>
        <el-table-column prop="description" label="接口数量" sortable></el-table-column>
        <el-table-column label="计划">
          <template slot-scope="scope">
            <el-button @click="setting" size="small">设置</el-button>
          </template>
        </el-table-column>
        <el-table-column prop="status" label="状态">
        <template slot-scope="scope">
          <el-switch
              v-model="scope.row.status"
              active-color="#13ce66"
              inactive-color="#ff4949">
            </el-switch>
        </template>
      </el-table-column>
        <el-table-column label="报告">
          <template slot-scope="scope">
            <el-button type="info" size="small">查看报告</el-button>
          </template>
        </el-table-column>
        <el-table-column label="操作">
          <template slot-scope="scope">
            <el-button type="primary" size="small">编辑</el-button>
            <el-button type="danger" size="small">删除</el-button>
          </template>
        </el-table-column>
      </el-table>
      <el-pagination layout="prev, pager, next" :page-size="20" :page-count="total"></el-pagination>
    </el-col>
    <el-dialog title="新增用例" :visible.sync="addTaskFormStatus" :close-on-click-modal="false">
        <el-form :model="taskForm" :rules="taskFormRules" label-width="80px">
            <el-form-item label="项目:">
               <el-select v-model='taskForm.project' placeholder='所属模块'>
              <el-option v-for='(item,index) in project' :key='index' :label='el-form-itemem.label' :value='item.value'></el-option>
              </el-select>
            </el-form-item><el-form-item label="用例名称:" prop="reportFrom">
                <el-input v-model.trim="taskForm.reportFrom" auto-complete="off"></el-input>
            </el-form-item>
            <el-form-item label="描述:" prop="mailUser">
                <el-input v-model.trim="taskForm.mailUser" auto-complete="off"></el-input>
            </el-form-item>
        </el-form>
        <div slot="footer" class="dialog-footer">
            <el-button @click.native="addTaskFormStatus = false">取消</el-button>
            <el-button type="primary" @click="addTaskForm" :loading="loading">提交</el-button>
        </div>
    </el-dialog>
    <el-dialog title="定时用例" :visible.sync="settingFormStatus"  :close-on-click-modal="false" >
            <el-form ref="form" :model="form">
                <el-form-item label="计划时间" prop="time">
                    <el-date-picker v-model="form.time" type="datetime" placeholder="选择日期时间"></el-date-picker>
                </el-form-item>
                <el-form-item label="执行环境" prop="Host">
                    <el-select v-model="form.Host"  placeholder="测试环境">
                        <el-option v-for="(item,index) in Host" :key="index+''" :label="item.name" :value="item.id"></el-option>
                    </el-select>
                </el-form-item>
                <el-form-item label="循环次数" prop="Host">
                    <el-input v-model.number="form.frequency" placeholder="循环次数"></el-input>
                </el-form-item>
                <el-form-item>
                    <el-button type="primary" @click="setTaskStart">开始</el-button>
                    <el-button type="primary" @click="setTaskStop">停用</el-button>
                </el-form-item>
            </el-form>
        </el-dialog>
  </el-row>
</template>

<script>
  export default{
    data(){
      return{
        total:0,
        loading:false,
        listLoading:false,
        addTaskFormStatus:false,
        settingFormStatus:false,
        taskFormRules: {},
        taskForm:{},
        project:[],
        Host:[],
        form: {
            name: "",
            timeArray: [],
            Host: "",
        },
        taskList:[]
      }
    },
    methods:{
      getTaskList(){
        this.taskList = [{name:'Test'}]
      },
      addTask(){
        this.addTaskFormStatus=true
      },
      setting(){
        this.settingFormStatus=true
      },
      setTaskStart(){
        this.settingFormStatus=false
      },
      setTaskStop(){
        this.settingFormStatus=false
      },
      addTaskForm(){
        this.addTaskFormStatus=false
      }
    },
    mounted(){
      this.getTaskList()
    }
  }
</script>