<template>
  <el-row>
    <el-col :span="24">
      <el-row>
      <el-col :span='24'>
        <el-button type='primary' @click='addMock'>新增数据</el-button>
      </el-col>
    </el-row>
      <el-table :data="mockList" highlight-current-row v-loading="listLoading">
        <el-table-column prop="name" label="名称" sortable></el-table-column>
        <el-table-column prop="variable" label="变量" sortable></el-table-column>
        <el-table-column prop="type" label="类型" sortable></el-table-column>
        <el-table-column prop="source" label="来源" sortable></el-table-column>
        <el-table-column label="操作">
          <template slot-scope="scope">
            <el-button type="primary" size="small">编辑</el-button>
            <el-button type="danger" size="small">删除</el-button>
          </template>
        </el-table-column>
      </el-table>
      <el-pagination layout="prev, pager, next" :page-size="20" :page-count="total"></el-pagination>
    </el-col>
    <el-dialog title="新增数据" :visible.sync="addMockFormStatus" :close-on-click-modal="false">
        <el-form :model="mockForm" :rules="mockFormRules" :inline="true">
            <el-form-item label="来源">
                <template>
                  <el-radio-group v-model="mockForm.source">
                    <el-radio label="1">本地模拟</el-radio>
                    <el-radio label="2">文件(csv)</el-radio>
                  </el-radio-group>
                </template>
            </el-form-item>
            <el-form-item label="类型">
               <el-select v-model='mockForm.type' placeholder='类型'>
              <el-option v-for='(item,index) in type' :key='index' :label='item.label' :value='item.value'></el-option>
              </el-select>
            </el-form-item><el-form-item label="变量名称" prop="variable">
                <el-input v-model.trim="mockForm.variable" auto-complete="off"></el-input>
            </el-form-item>
            <el-form-item label="长度" prop="length">
                <el-input v-model.trim="mockForm.length" auto-complete="off"></el-input>
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
        </el-form>
        <div slot="footer" class="dialog-footer">
            <el-button @click.native="addMockFormStatus = false">取消</el-button>
            <el-button type="primary" @click="addMockForm" :loading="loading">提交</el-button>
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
        addMockFormStatus:false,
        settingFormStatus:false,
        mockFormRules: {},
        mockForm:{},
        type:[{label:'字母',value:'0'},{label:'数字',value:'1'},{label:'日期',value:'2'},{label:'符号',value:'3'}],
        fileList:[],
        form: {
            variable: "",
            length:0
        },
        mockList:[]
      }
    },
    methods:{
      getMockList(){
        this.mockList = [{name:'Test'}]
      },
      addMock(){
        this.addMockFormStatus=true
      },
      addMockForm(){
        this.addMockFormStatus=false
      },
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
    },
    mounted(){
      this.getMockList()
    }
  }
</script>