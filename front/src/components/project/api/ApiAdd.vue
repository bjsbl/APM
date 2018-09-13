<template>
  <section>
    <el-form :model='form' label-width="80px">
      <el-form-item>
          <el-button type="primary" @click="showVariable">添加变量</el-button>
          <el-button type="primary" @click="addApi">保存</el-button>
          <el-button type="primary" @click="goApi">返回</el-button>
      </el-form-item>
      <el-row>
        <el-col :span="16">
          <el-form-item label='接口名称:' prop='name'>
            <el-input v-model.trim='form.name' placeholder='名称' ></el-input>
          </el-form-item>
        </el-col>
        <el-col :span="8">
          <el-form-item label='模块:' prop='module'>
            <el-select v-model='form.module' placeholder='所属模块'>
              <el-option v-for='(item,index) in module' :key='index' :label='item.label' :value='item.value'></el-option>
            </el-select>
          </el-form-item>
        </el-col>
      </el-row>
      <el-row>
        <el-col :span="8">
          <el-form-item label='状态:' prop='status'>
            <el-select v-model='form.status' placeholder='接口状态'>
              <el-option v-for='(item,index) in status' :key='index' :label='item.label' :value='item.value'></el-option>
            </el-select>
          </el-form-item>
        </el-col>
        <el-col :span="8">
          <el-form-item label='HTTP协议:' prop='httpType'>
            <el-select v-model='form.httpType' placeholder='HTTP协议'>
              <el-option v-for='(item,index) in Http' :key='index'  :label='item.label' :value='item.value'></el-option>
            </el-select>
          </el-form-item>
        </el-col>
        <el-col :span="8">
          <el-form-item label='请求方式:' prop='request'>
            <el-select v-model='form.method' placeholder='请求方式'>
              <el-option v-for='(item,index) in request' :key='index' :label='item.label' :value='item.value'></el-option>
            </el-select>
          </el-form-item>
        </el-col>
      </el-row>
      <el-form-item prop="apiAddress" label='请求地址:'>
          <el-input v-model.trim="form.apiAddress" placeholder="地址" auto-complete></el-input>
      </el-form-item>
      <el-row :span="24">
         <el-collapse v-model="activeNames">
           <el-collapse-item title="请求头部" name='a'>
              <el-table :data="form.headerList" highlight-current-row>
                <el-table-column prop="name" label="标签">
                  <template slot-scope="scope">
                    <el-select v-model="scope.row._type" placeholder="head标签">
                      <el-option v-for='(item,index) in header' :key='index' :label='item.label' :value='item.value'></el-option>
                    </el-select>
                  </template>
                </el-table-column>
                <el-table-column prop="value" label="内容">
                  <template slot-scope="scope">
                    <el-input placeholder="请输入内容"></el-input>
                  </template> 
                </el-table-column>
                <el-table-column label="操作">
                  <template slot-scope="scope">
                    <el-button @click='delHeader(scope.$index)'>删除</el-button>
                    <el-button @click='addHeader'>添加</el-button>
                  </template>
                </el-table-column>
              </el-table>
           </el-collapse-item>
           <el-collapse-item title="请求参数" name='b'>
              <section>
                <template>
                  <el-radio-group v-model="radio" @change="requestTypeChange">
                    <el-radio label="form-data">form-data</el-radio>
                    <el-radio label="www-form-urlencoded">x-www-form-urlencoded</el-radio>
                    <el-radio label="raw">raw</el-radio>
                  </el-radio-group>
                </template>
              </section>
              <section v-show="isRaw">
               <template>
                  <el-input type="textarea" :rows="5" placeholder="请输入内容" v-model.trim="form.raw"></el-input>
              </template>
              </section>
              <el-table v-show="!isRaw" :data="form.requestList" highlight-current-row>
                <el-table-column prop='name' label='参数名'>
                  <template slot-scope="scope">
                    <el-input placeholder='请输入参数值'></el-input>
                  </template>
                </el-table-column>
                <el-table-column prop='value' label='参数值'>
                  <template slot-scope="scope">
                    <el-input placeholder='请输入参数值' v-show="!isFile"></el-input>
                    <el-upload action="@" v-show="isFile">
                      <el-button size="small" type="primary">点击上传</el-button>
                    </el-upload>
                  </template>
                </el-table-column>
                <el-table-column prop='_type' label='参数类型'>
                  <template slot-scope="scope">
                  <el-select v-model="scope.row._type" placeholder='请求方式' @change="parameterTypeChange">
                    <el-option v-for='(item,index) in paramType' :key='index' :label='item.label' :value='item.value'></el-option>
                  </el-select>
                </template>
                </el-table-column>
                <el-table-column prop="required" label="必填" >
                  <template slot-scope="scope">
                    <el-select v-model="scope.row.required" placeholder="必填">
                        <el-option v-for="(item,index) in required" :key="index+''" :label="item.label" :value="item.value"></el-option>
                    </el-select>
                  </template>
                </el-table-column>
                <el-table-column prop='description' label='参数说明'>
                  <template slot-scope="scope">
                  <el-input placeholder='请输入参数说明'></el-input>
                </template>
                </el-table-column>
                <el-table-column label="操作">
                    <template slot-scope="scope">
                      <el-button @click='delRequest(scope.$index)'>删除</el-button>
                      <el-button @click='addRequest'>添加</el-button>
                    </template>
                  </el-table-column>
              </el-table>
           </el-collapse-item>
           <el-collapse-item title="返回参数" name="c">
              <el-table :data="form.responseList" highlight-current-row>
                <el-table-column prop='name' label='参数名'>
                  <template slot-scope="scope">
                    <el-input placeholder='请输入参数值'></el-input>
                  </template>
                </el-table-column>
                <el-table-column prop='value' label='参数值'>
                  <template slot-scope="scope">
                    <el-input placeholder='请输入参数值'></el-input>
                  </template>
                </el-table-column>
                <el-table-column prop='_type' label='参数类型'>
                  <template slot-scope="scope">
                    <el-select v-model="scope.row._type" placeholder='请求方式'>
                      <el-option v-for='(item,index) in paramType' :key='item.value' :label='item.label'  :value='item.value'></el-option>
                    </el-select>
                  </template>
                </el-table-column>
                <el-table-column prop='description' label='参数说明'>
                  <template slot-scope="scope">
                    <el-input placeholder='请输入参数说明'></el-input>
                  </template>
                </el-table-column>
                <el-table-column label="操作">
                    <template slot-scope="scope">
                      <el-button @click='delResponse(scope.$index)'>删除</el-button>
                      <el-button @click='addResponse'>添加</el-button>
                    </template>
                  </el-table-column>
              </el-table>
           </el-collapse-item> 
           <el-collapse-item title="备注" name="d">
              <el-input type="textarea" :rows="7" placeholder="请输入描述"></el-input>
           </el-collapse-item>
          </el-collapse>
      </el-row>
    </el-form>
    <el-dialog title="选择变量" :visible.sync="addVariableVisible" :close-on-click-modal="false" >
        <el-row>
            <el-col :span="18">
                <el-table :data="variableList" highlight-current-row v-loading="listLoading">
                    <el-table-column type="selection"></el-table-column>
                    <el-table-column prop="name" label="名称" min-width="25%" sortable>
                    </el-table-column>
                    <el-table-column prop="requestType" label="类型" min-width="15%" sortable>
                    </el-table-column>
                    <el-table-column prop="apiAddress" label="规则" min-width="60%" sortable>
                    </el-table-column>
                </el-table>
            </el-col>
        </el-row>
        <el-col :span="24" class="toolbar">
            <el-pagination layout="prev, pager, next" :page-size="20" :page-count="total"></el-pagination>
        </el-col>
        <div slot="footer" class="dialog-footer">
            <el-button @click.native="addVariableVisible = false">取消</el-button>
            <el-button type="primary" @click="addVariableForm">提交</el-button>
        </div>
      </el-dialog>
  </section>
</template>
<script>
  export default{
    data(){
      return {
        activeNames: ['d'],
        fileList:[],
        isRaw:false,
        isFile:false,
        addVariableVisible:false,
        listLoading:false,
        module:[],
        variableList:[],
        radio:"form-data",
        request: [{value: 'GET', label: 'GET'},{value: 'POST', label: 'POST'},{value: 'PUT', label: 'PUT'},{value: 'DELETE', label: 'DELETE'}],
        Http: [{value: 'HTTP', label: 'HTTP'},{value: 'HTTPS', label: 'HTTPS'}],
        paramType: [{value: 'Text', label: 'Text'},{value: 'File', label: 'File'}],
        status: [{value: true, label: '启用'},{value: false, label: '禁用'}],
        required:[{value: true, label: '是'},{value: false, label: '否'}],
        header: [{value: 'Accept', label: 'Accept'},
        {value: 'Accept-Charset', label: 'Accept-Charset'},
        {value: 'Accept-Encoding', label: 'Accept-Encoding'},
        {value: 'Accept-Language', label: 'Accept-Language'},
        {value: 'Accept-Ranges', label: 'Accept-Ranges'},
        {value: 'Authorization', label: 'Authorization'},
        {value: 'Cache-Control', label: 'Cache-Control'},
        {value: 'Connection', label: 'Connection'},
        {value: 'Cookie', label: 'Cookie'},
        {value: 'Content-Length', label: 'Content-Length'},
        {value: 'Content-Type', label: 'Content-Type'},
        {value: 'Content-MD5', label: 'Content-MD5'},
        {value: 'Date', label: 'Date'},
        {value: 'Expect', label: 'Expect'},
        {value: 'From', label: 'From'},
        {value: 'Host', label: 'Host'},
        {value: 'If-Match', label: 'If-Match'},
        {value: 'If-Modified-Since', label: 'If-Modified-Since'},
        {value: 'If-None-Match', label: 'If-None-Match'},
        {value: 'If-Range', label: 'If-Range'},
        {value: 'If-Unmodified-Since', label: 'If-Unmodified-Since'},
        {value: 'Max-Forwards', label: 'Max-Forwards'},
        {value: 'Origin', label: 'Origin'},
        {value: 'Pragma', label: 'Pragma'},
        {value: 'Proxy-Authorization', label: 'Proxy-Authorization'},
        {value: 'Range', label: 'Range'},
        {value: 'Referer', label: 'Referer'},
        {value: 'TE', label: 'TE'},
        {value: 'Upgrade', label: 'Upgrade'},
        {value: 'User-Agent', label: 'User-Agent'},
        {value: 'Via', label: 'Via'},
        {value: 'Warning', label: 'Warning'}],
        form:{
          name:'',
          requestType:'form-data',
          status:'',
          method:'',
          module:[],
          headerList:[{name:'1',value:'2'}],
          requestList:[{name: '', value: '', _type:'Text', required: 'true',description: ''}],
          responseList:[{name: '', value: '', _type:'Text',description: ''}]
        }
      }
    },
    methods:{
      showVariable(){
        this.addVariableVisible = true
      },
      addVariableForm(){
        this.addVariableVisible = false
      },
      requestTypeChange(e){
        this.requestType = e
        if(e=='form-data'){
          this.isRaw=false
          this.paramType=[{value: 'Text', label: 'Text'},{value: 'File', label: 'File'}]
        }else if(e=='www-form-urlencoded'){
          this.paramType=[{value: 'Text', label: 'Text'}]
          this.isRaw=false
        }else if(e=='raw'){
          this.isRaw=true
        }
      },
      parameterTypeChange(e){
        if(e=='File'){
          this.isFile = true
        }else{
          this.isFile = false
        }
      },
      addHeader(){
        this.form.headerList.push({name:'',value:''})
      },
      delHeader(index){
        this.form.headerList.splice(index,1)
        if(this.form.headerList.length==0){
          this.form.headerList.push({name:'',value:''})
        }
      },
      addRequest(){
        this.form.requestList.push({name:'',value:'',_type:'String',required:'true',description:''})
      },
      delRequest(index){
        this.form.requestList.splice(index,1)
        if(this.form.requestList.length==0){
          this.form.requestList.push({name:'',value:'',_type:'String',required:'true',description:''})
        }
      },
      addResponse(){
        this.form.responseList.push({name:'',value:'',_type:'String',description:''})
      },
      delResponse(index){
        this.form.responseList.splice(index,1)
        if(this.form.responseList.length==0){
          this.form.responseList.push({name:'',value:'',_type:'String',description:''})
        }
      },
      addApi(){
        this.$notify({
          title: '成功',
          message: '这是一条成功的提示消息',
          type: 'success'
        });
      },
      goApi(){
        this.$router.push('/api/list/1')
      }
    }
  }
</script>