class TerminatorBaseClass:



    @classmethod
    def terminate_scraper(cls, dependencies):
        dependencies.sqs_messager.send_completion_message_to_aws(
            logger=dependencies.logger.logger,
            outlet_id=dependencies.settings.outlet_id,
            worker_queue_url=dependencies.settings.worker_queue_url
        )
        dependencies.logger.sqs_message_log()
        dependencies.state.status = "Finished"
        if dependencies.settings.live_status is True:   
            dependencies.state.reset_price_count()
            dependencies.state.reset_input_count()
        dependencies.state.save_state(dependencies)
        return
