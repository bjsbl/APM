<template>
  <el-row>
    <el-col :span="24">
      <el-row>
      <el-col :span='24'>
        <el-button type='primary' @click='addScript'>新增脚本</el-button>
      </el-col>
    </el-row>
      <el-table :data="scriptList" highlight-current-row v-loading="listLoading">
        <el-table-column prop="name" label="名称" sortable>
        </el-table-column>
        <el-table-column prop="uploadTime" label="上传时间" sortable></el-table-column>
        <el-table-column prop="status" label="状态">
        <template slot-scope="scope">
          <el-switch
              v-model="scope.row.status"
              active-color="#13ce66"
              inactive-color="#ff4949">
            </el-switch>
        </template>
      </el-table-column>
        <el-table-column label="源文件">
          <template slot-scope="scope">
            <el-button type="info" size="small">查看源文件</el-button>
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
    <el-dialog title="新增脚本" :visible.sync="addScriptFormStatus" :close-on-click-modal="false">
        <el-form :model="scriptForm" :rules="scriptFormRules" label-width="80px">
            <el-form-item label="脚本名称:" prop="reportFrom">
                <el-input v-model.trim="scriptForm.reportFrom" auto-complete="off"></el-input>
            </el-form-item>
            <el-form-item>
              <el-upload
                class="upload-demo"
                action="https://jsonplaceholder.typicode.com/posts/"
                :on-preview="handlePreview"
                :on-remove="handleRemove"
                :before-remove="beforeRemove"
                multiple
                :limit="3"
                :on-exceed="handleExceed"
                :file-list="fileList">
                <el-button size="small" type="primary">点击上传</el-button>
                <div slot="tip" class="el-upload__tip">只能上传jpg/png文件，且不超过500kb</div>
              </el-upload>
            </el-form-item>
            <el-form-item label="描述:" prop="mailUser">
                <el-input v-model.trim="scriptForm.mailUser" auto-complete="off"></el-input>
            </el-form-item>
        </el-form>
        <div slot="footer" class="dialog-footer">
            <el-button @click.native="addScriptFormStatus = false">取消</el-button>
            <el-button type="primary" @click="addScriptForm" :loading="loading">提交</el-button>
        </div>
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
        addScriptFormStatus:false,
        settingFormStatus:false,
        scriptFormRules: {},
        scriptForm:{},
        Host:[],
        fileList:[],
        form: {
            name: "",
            project:[],
            timeArray: [],
            Host: "",
        },
        scriptList:[]
      }
    },
    methods:{
      handleRemove(file, fileList) {
        console.log(file, fileList);
      },
      handlePreview(file) {
        console.log(file);
      },
      handleExceed(files, fileList) {
        this.$message.warning(`当前限制选择 3 个文件，本次选择了 ${files.length} 个文件，共选择了 ${files.length + fileList.length} 个文件`);
      },
      beforeRemove(file, fileList) {
        return this.$confirm(`确定移除 ${ file.name }？`);
      },
      getScriptList(){
        this.scriptList = [{name:'Test'}]
      },
      addScript(){
        this.addScriptFormStatus=true
      },
      addScriptForm(){
        
      }
    },
    mounted(){
      this.getScriptList()
    }
  }
</script>