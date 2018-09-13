<template>
  <el-row>
    <el-col :span="24">
      <el-row>
      <el-col :span='24'>
        <el-button type='primary' @click='addAgent'>新增代理</el-button>
      </el-col>
    </el-row>
      <el-table :data="agentList" highlight-current-row v-loading="listLoading">
        <el-table-column prop="name" label="名称" sortable></el-table-column>
        <el-table-column prop="host" label="主机" sortable></el-table-column>
        <el-table-column prop="system" label="系统" sortable></el-table-column>
        <el-table-column prop="lastUpdateTime" label="最新修改时间" sortable></el-table-column>
      </el-table>
      <el-pagination :current-page="1"layout="prev, pager, next" :page-size="20" :page-count="total"></el-pagination>

      <el-dialog title="添加代理" :visible.sync="addAgentVisible" :close-on-click-modal="false" >
        <el-form label-width="80px" v-model="agentForm">
        <el-form-item label='名称'>  
          <el-input type='text' auto-complete="off" v-model.trim="agentForm.name"></el-input>
        </el-form-item>
        <el-form-item label='主机'>  
          <el-input type='text' auto-complete="off" v-model.trim="agentForm.name"></el-input>
        </el-form-item>
      </el-form>
          <div slot="footer" class="dialog-footer">
            <el-button @click="addAgentVisible = false">取消</el-button>
            <el-button type="primary" @click="addAgentForm" :loading="addLoading">下载代码</el-button>
          </div>
      </el-dialog>
    </el-col>
  </el-row>
</template>

<script>
  export default{
    data(){
      return{
        total:0,
        listLoading:false,
        addLoading:false,
        moduleListLoading:false,
        addAgentVisible:false,
        moduleList:[],
        agentList:[],
        agentForm:{
          name:'',
          description:''
        }
      }
    },
    methods:{
      getGroupList(){
        let _this = this
        _this.ajax.get("/static/mock/agent.json").then(function(res){
          _this.agentList = res.data.result.data
        })
      },
      addAgent(){
        this.addAgentVisible=true
      },
      addAgentForm(){
        this.addAgentVisible=false
      }
    },
    mounted(){
      this.getGroupList()
    }
  }
</script>