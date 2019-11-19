% rebase('layout.tpl', title='Home Page', year=year)
<style>
.bsz2{
    width: 137px;
    height: 70px;
    font-size: small;
    margin: 2px !important;
}
</style>
    <main role="main">

      <!-- Main jumbotron for a primary marketing message or call to action -->
      <div class="jumbotron">
        <div class="container">
          <h1 class="display-3">Home Control</h1>
        </div>
      </div>

      <div class="container">
      </div> <!-- /container -->
		%for x in js:
		<button class='btn btn-primary bsz2' id='{{x[0]}}'>{{x[1]}}</button>
		%end
		<script>
		$(function(){
			$('.bsz2').click(function(){
				var id=$(this).attr('id');
				console.log(id);
				$.get('/click/'+id, function(data){
					console.log(data);
				})
			});
		});
		</script>
    </main>
