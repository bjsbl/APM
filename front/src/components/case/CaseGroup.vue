<template>
  <el-row>
    <el-col :span="24">
      <el-row>
      <el-col :span='24'>
        <el-button type='primary' @click='addCaseGroup'>新增分组</el-button>
      </el-col>
    </el-row>
      <el-table :data="caseGroupList" highlight-current-row v-loading="listLoading">
        <el-table-column prop="name" label="名称" sortable></el-table-column>
        <el-table-column prop="description" label="描述" sortable></el-table-column>
      </el-table>
      <el-pagination layout="prev, pager, next" :page-size="20" :page-count="total"></el-pagination>

      <el-dialog title="添加分组" :visible.sync="addCaseGroupVisible" :close-on-click-modal="false" >
        <el-form label-width="80px" v-model="groupForm">
        <el-form-item label='名称'>  
          <el-input type='text' auto-complete="off" v-model.trim="groupForm.name"></el-input>
        </el-form-item>
        <el-form-item label='描述'>  
          <el-input type="textarea" :rows="5" v-model.trim="groupForm.description"></el-input>
        </el-form-item>
      </el-form>
          <div slot="footer" class="dialog-footer">
            <el-button @click="addCaseGroupVisible = false">取消</el-button>
            <el-button type="primary" @click="addCaseGroupForm" :loading="addLoading">提交</el-button>
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
        addCaseGroupVisible:false,
        moduleList:[],
        caseGroupList:[],
        groupForm:{
          name:'',
          description:''
        }
      }
    },
    methods:{
      getGroupList(){
        let _this = this
        _this.ajax.get("/static/mock/projectmodule.json").then(function(res){
          _this.caseGroupList = res.data.result.data
        })
      },
      addCaseGroup(){
        this.addCaseGroupVisible=true
      },
      addCaseGroupForm(){
        this.addCaseGroupVisible=false
      }
    },
    mounted(){
      this.getGroupList()
    }
  }
</script>