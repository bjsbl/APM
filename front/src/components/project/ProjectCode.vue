<template>
  <el-row>
    <el-col :span="24">
      <el-row>
      <el-col :span='24'>
        <el-form :inline="true" :model="filters">
        <el-form-item>
          <el-input v-model.trim="filters.name" placeholder="名称"></el-input>
        </el-form-item>
        <el-form-item>
          <el-button type="primary" @click="getProjectCodeList">查询</el-button>
        </el-form-item>
       <el-form-item>
        <el-button type='primary' @click='addProjectCode'>新增状态码</el-button>
      </el-form-item>
      </el-form>
      </el-col>
    </el-row>
      <el-table :data="projectCodeList" highlight-current-row v-loading="listLoading">
        <el-table-column prop="name" label="编码" sortable></el-table-column>
        <el-table-column prop="message" label="说明" sortable></el-table-column>
        <el-table-column prop="user" label="创建人" sortable></el-table-column>
        <el-table-column prop="lastUpdateTime" label="更新时间" sortable></el-table-column>
        <el-table-column label="操作">
          <template slot-scope="scope">
            <el-button size="small">编辑</el-button>
            <el-button type="danger" size="small">删除</el-button>
          </template>
        </el-table-column>
      </el-table>
      <el-pagination layout="prev, pager, next" :page-size="20" :page-count="total"></el-pagination>

      <el-dialog title='新增' :close-on-click-modal='false' :visible.sync='addProjectCodeVisible'>
      <el-form label-width="80px" v-model="codeForm">
        <el-form-item label='编码'>  
          <el-input type='text' auto-complete="off" v-model.trim="codeForm.code"></el-input>
        </el-form-item>
        <el-form-item label='描述'>  
          <el-input type="textarea" :rows="5" v-model.trim="codeForm.message"></el-input>
        </el-form-item>
      </el-form>
          <div slot="footer" class="dialog-footer">
            <el-button @click="addProjectCodeVisible = false">取消</el-button>
            <el-button type="primary" @click="addProjectCodeForm" :loading="addLoading">提交</el-button>
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
        addProjectCodeVisible:false,
        memberList:[],
        projectCodeList:[],
        filters:{
          name:''
        },
        codeForm:{
          name:'',
          message:''
        }
      }
    },
    methods:{
      getProjectCodeList(){
        let _this = this
        _this.ajax.get("/static/mock/projectcode.json").then(function(res){
          _this.projectCodeList = res.data.result.data
        })
      },
      addProjectCode(){
        this.addProjectCodeVisible=true
      },
      addProjectCodeForm(){
        this.addProjectCodeVisible=false
      }
    },
    mounted(){
      this.getProjectCodeList()
    }
  }
</script>